import operator
import math
    
def clean(L):
    if isinstance(L, list):
        return [x for x in L if x]
    if isinstance(L, dict):
        return {k:v for k,v in L.items() if v}

FRUITS = {'apple', 'peach', 'banana', 'cherry', 'orange', 'pear', 'kiwi'}
GRADES = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E+', 'E', 'F']
USERS = {'alice', 'bob', 'carl'}

rankings = {
    'alice': 
    {
        'B+': ['cherry', 'orange'], 
        'D': ['banana', 'apple', 'kiwi']
    },
    
    'bob': 
    {
        'B+': ['orange'], 
        'D+': ['kiwi', 'pear'], 
        'D': ['apple', 'banana']
    },
    
    'carl': {
        'A+': ['pear', 'apple'], 
        'A': ['cherry'], 
        'C+': ['peach'], 
        'C': ['orange', 'kiwi'], 
        'F': ['banana']
    }
}

def to_rating_dict(L):
    length = len(L)
    return {key: (length-i)/float(length) for i, key in enumerate(L)}

def mean(L):
    L2 = [x for x in L if x]
    return sum(L2)/float(len(L2))
    
def in_interval(a, b, x):
    return x>a and x<=b
    
def variance(L):
    def square(x): return x*x
    return sum(map(square, L)) / float(len(L))
    
def std(L):
    return math.sqrt(variance(L))
    
grade_bases = to_rating_dict(GRADES)

fruit_user_ratings = {fruit: {} for fruit in FRUITS}
user_fruit_ratings = {user : {} for user  in USERS }

for user in USERS:
    print('\nuser: {} '.format(user) + 40*'-')
    user_ranking = rankings[user]
    for grade in GRADES:
        if grade in user_ranking.keys():
            print('grade')
            print(grade)
            gb = grade_bases[grade]
            l = user_ranking[grade]
            r = to_rating_dict(l)
            print('r')
            print(r)
            for fruit, step_rating in r.items():
                print('*',fruit, step_rating)
                fr = gb-(1-step_rating)/len(GRADES)
                fruit_user_ratings[fruit][user] = fr
                user_fruit_ratings[user][fruit] = fr

#########################

fruit_user_ratings_means = {fruit: mean(rating_dict.values()) for fruit, rating_dict in fruit_user_ratings.items()}
fruit_user_ratings_means_sorted = sorted(fruit_user_ratings_means.items(), key=operator.itemgetter(1))

print(user_fruit_ratings)

diff_abs = {f:[] for f in FRUITS}

print('')
print('mean:')
print(fruit_user_ratings_means)
for user in USERS:
    print('')
    print(user+':')
    for fruit in FRUITS:
        print('fruit')
        print(fruit)
        if fruit in user_fruit_ratings[user].keys():
            print(user_fruit_ratings[user][fruit])
            diff_abs_user = abs(fruit_user_ratings_means[fruit]-user_fruit_ratings[user][fruit])
            diff_abs[fruit].append(diff_abs_user)
            print(diff_abs_user)
   
for f, v in diff_abs.items():
    print(f)
    print(v)
    print(variance(v))
    print(std(v))

### compute coarse ratings for fruits
for f, r in fruit_user_ratings_means.items():
    for i in range(len(GRADES)):
        grade_i = GRADES[i]
        a=grade_bases[grade_i]
        b=grade_bases[GRADES[i+1]] if i<len(GRADES)-1 else 0
        if in_interval(b, a, r):
            print('{} is ranked {}'.format(f, grade_i))
    
