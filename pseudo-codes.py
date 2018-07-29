import operator
import math

VARIANCE_HALF = 0.01

## utility functions
def to_rating_dict(L): 
    return {key: float(len(L)-i)/len(L) for i, key in enumerate(L)}

def is_in_interval(x, a, b): 
    return a<x and x<=b

def mean(L): 
    return sum(L) / float(len(L))

def variance(L): 
    L2 = map(lambda x: x*x, L)
    return mean(L2)

def model(v): 
    return 1 / (1 + v / VARIANCE_HALF)

## example ranking data (of fruits)
FRUITS = {'apple', 'peach', 'banana', 'cherry', 'orange', 'pear', 'kiwi'}
GRADES = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E+', 'E', 'F']
USERS = {'Alice', 'Bob', 'Carl'}

rankings = {
    'Alice': 
    {
        'B+': ['cherry', 'orange'], 
        'D': ['banana', 'apple', 'kiwi']
    },
    
    'Bob': 
    {
        'B+': ['orange'], 
        'D+': ['kiwi', 'pear'], 
        'D': ['apple', 'banana']
    },
    
    'Carl': {
        'A+': ['pear', 'apple'], 
        'A': ['cherry'], 
        'C+': ['peach'], 
        'C': ['orange', 'kiwi'], 
        'F': ['banana']
    }
}
    
## collect data
grade_bases = to_rating_dict(GRADES)

fruit_user_ratings = {fruit: {} for fruit in FRUITS}
user_fruit_ratings = {user : {} for user  in USERS }

for user in USERS:
    print('\nuser: {} '.format(user) + 40*'-')
    user_ranking = rankings[user]
    for grade in GRADES:
        if grade in user_ranking.keys():
            gb = grade_bases[grade]
            l = user_ranking[grade]
            r = to_rating_dict(l)
            for fruit, step_rating in r.items():
                fr = gb-(1-step_rating)/len(GRADES)
                fruit_user_ratings[fruit][user] = fr
                user_fruit_ratings[user][fruit] = fr

## compute bracketed means
fruit_user_ratings_means = {fruit: mean(rating_dict.values()) for fruit, rating_dict in fruit_user_ratings.items()}
fruit_user_ratings_means_sorted = sorted(fruit_user_ratings_means.items(), key=operator.itemgetter(1))

## voting "game"                 
diff_abs = {u: {} for u in USERS}

for user in USERS:
    for fruit in FRUITS:
        if fruit in user_fruit_ratings[user].keys():
            diff_abs[user][fruit] = abs(fruit_user_ratings_means[fruit]-user_fruit_ratings[user][fruit])

user_absch = {u: model(variance(udiffs.values())) for u, udiffs in diff_abs.items()}
user_absch_normed = {u: v / sum(user_absch.values()) for u, v in user_absch.items()}

print(user_absch_normed)

### compute coarse ratings for fruits
for f, r in fruit_user_ratings_means.items():
    for i in range(len(GRADES)):
        i_grade = GRADES[i]
        b = grade_bases[i_grade]
        a = grade_bases[GRADES[i+1]] if i<len(GRADES)-1 else 0
        if is_in_interval(r, a, b):
            print('{} is ranked {}'.format(f, grade_i))
    
