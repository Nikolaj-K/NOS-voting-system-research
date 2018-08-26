# "Voting Paper" section Abstract (notes, comments upfront)

## Terminology and fundamental notions
1) Basic summary of 
	* what we want to design.
	* companies that have something similar. 
	* what's different here
		a) blockchain consensus
		b) dApp rankings
		
1.1) Gain from being votes high up.

2) We're first going to give an overview of properties of voting systems (viewed on their own). 

3) Then rule out and classify for the means of a) and b)

4) Differentiate between existing voting systems (that exhibit properties). 

5) Also point out how those apply for the other companies.

6) Propose an algorithm based on our considerations.


## Resources

###### Books
The mathematics of voting and elections: A hands-on approach.

###### Why voting dApps isn't voting parties
The "Handbook of Electoral System Choice" (by Josep M. Colomer, Georgetown University) covers the selection of voting systems, but that treatie is about setling the joicy of political electoral system to determine parties from and for countries. In contrast, highly voted apps benefit from exposure but are not voted into the status of rule makers.

Furthermore, we don't have winners as such, but instead obtain exposure.


###### "Electorama" Wiki 
This wiki is designed to give "election-minded" people an overview of different electoral systems, because the system chosen for the election has great influence on the election's outcome. 

* Main page
https://wiki.electorama.com 

* All pages:
https://wiki.electorama.com/wiki/Special:AllPages

	
###### "Electoral Knowledge Network" website (todo)
This website provides information and customised advice on electoral processes. 
The "Administration and Cost of Elections" (short: "ACE") - Projects promotes electoral processes the project's team considers credible and transparent. 
Besides other information, the website contains global statistics and data and an Enyclopaedia of Elections which covers topics in elections management. 
http://www.aceproject.org/ 
http://aceproject.org/ace-en

###### Wikipedia:

##### First-past-the-post voting/Winner takes it all
- Voters indicate on a ballot the candidate of their choice, and the candidate who receives the most votes wins. 
- If there are at least two positions two be filled, each voter casts (up to) the same number of votes as there are positions to be filled, and those elected are the highest-placed candidates corresponding to that number of positions. 
- (huge downside: it very much encourages tactical voting)
- https://en.wikipedia.org/wiki/First-past-the-post_voting 

##### Majority judgement
- Used to determine a single winner. 
- Voters grade each candidate in one of several ranks, for instance named from "excellent" to "bad", and the candidate with the highest median grade is the winner.
- The system's inventors mathematically proved that the system was the most "strategy-resistant" and therefore somehow immune to tactical voting.
- The algorithm we propose is also based on the median grade. 
https://en.wikipedia.org/wiki/Majority_judgment

##### Approval voting
- Usually used to determine a single winner. 
- Each voter may select any number of candidates. The winner is the candidate who is selected ("approved") most often. 
- Variation: each voter may only select a predetermined number of candidates, otherwise this person's cast votes are invalid. 
- The algorithm we propose also allows each candidate to evaluate an arbitrary numer of candidates, but it is far from being some sort of approval voting. 
https://www.electology.org/approval-voting
https://de.wikipedia.org/wiki/Wahl_durch_Zustimmung


##### Closed list voting
- Used when positions are to be filled by members of the running parties. 
- Closed list voting: The voters only can vote for the parties. The elected parties have full decision over who of their members get the positions. 
In praxis, the order in which a party's list candidates get elected can also be predetermined by districts. Then the voting system is called a "local list" system.  

- These systems aren't of any use for our considerations. 
- https://en.wikipedia.org/wiki/Closed_list; https://en.wikipedia.org/wiki/Party-list_proportional_representation




#### Preferential voting/Preference voting: 
May refer to different election systems or groups of election systems. Some authors consider preferentiality to be one of the characteristics by which electoral systems can be evaluated and classified. 
Preferential voting may, for example, refer to ranked voting methods/ordinal voting systems, i.e. all election methods that involve ranking candidates in order of preference in a hierarchy on the ordinal scale, the most important ones being instant-runoff voting, single transferable vote and the Borda count. 
instant-runoff voting
range voting/score voting
open list
bucklin voting

##### Score voting/rate voting 
- Used to determine a single winner. 
- Voters rate candidates on a scale. The candidate with the highest rating wins.  
- Variations of score voting can use a score-style ballot to elect multiple candidates simultaneously.

TODOTODOTODO: comparison to majority judgement, approval voting and bucklin voting (similarities/differences)

##### Instant-runoff voting 
Used in single-seat elections with more than two candidates 
Voters rank all of the candidates in their personal order of preference
The candidate with the fewest first-choice-votes is eliminated. If there is more than one candidate with the fewest first-choice-votes, the second-choice-votes of these candidates are taken into consideration and so on in order to eliminate only one candidate per voting round. 
In the last voting round there are only two candidates left. The one who gets a majority of first-choice-votes wins the election. 
Variations: There are a few variations of Instant-runoff voting. For example, a candidate could be considered the winner as soon as he/she has a majority of first-choice-votes even though there are more than two candidates left. 

#### Open list voting
Voters have at least some influence on the order in which a party's candidates are elected. (Example: The candidates are the party's members. Each party has a rank of their members. If a party's candidate reaches a certain quota of the votes, he gets the position even if he's not at the top of the party's list.) 
Open list describes a certain family of voting systems for elections in which multiple candidates are elected through allocations to an electoral listing. What this family has in common is that voters have at least some influence on the order in which a party's candidates are elected. 
In "relatively closed" list systems, a candidate must get a full quota of votes to win a seat. There are various quotas that could be considered for this purpose. 
In "more open" list systems, that quota is so low that it's possible that more of a party's candidates achieve the quota than the total number of seats won by the party. Therefore it should be constituted in advance whether the party's list ranking or the total number of each candidates' votes takes precedence if this happens.
In the "most open" list system, the total number of votes each candidate has received utterly determines the election result. 
In a "free list" system/panachage electors even have more power over which candidates are elected than in the systems above, because each elector is given as many votes as there are seats to be filled and is allowed to cast more than one vote to the very same candidate.
https://en.wikipedia.org/wiki/Open_list; https://en.wikipedia.org/wiki/Party-list_proportional_representation

##### Bucklin voting/The Grand Junction System: 
- Usually used to determine a single winner. 
- Each voter ranks the candidates in ascending order, the first one being the favorite and the last one being the worst candidate. 
- To evaluate the votings, at first the prime rank is considered. Each candidate gains a score as high as the number of voters that ranked him first. If a candidate's total votes reach a majority (i.e. more than half of the number of voters), this candidate is the winner of the election. If not, the second rank is taken into consideration. 
- The number of votes each candidate received at the second rank is added to the number of votes from the first rank. If a candidates number of votes reaches the majority (i.e. more than half of the number of voters), this candidate wins the election. Otherwise the procedure continues until a candidate with a majority vote is found. The winner then is the candidate with the most votes accumulated.
https://en.wikipedia.org/wiki/Bucklin_voting 
https://de.wikipedia.org/wiki/Bucklin-Wahl
https://www.youtube.com/watch?v=CkIYZsJAvNQ

#### Ranked voting/Ordinal voting systems 
Ranked voting describes certain voting systems in which voters rank outcomes in a hierarchy on the ordinal scale (ordinal voting systems). 


#### cardinal voting systems todo 

https://de.wikipedia.org/wiki/Majority_Judgment
https://www.electology.org/score-voting
https://en.wikipedia.org/wiki/Score_voting 



https://en.wikipedia.org/wiki/Instant-runoff_voting (todo)
https://en.wikipedia.org/wiki/Open_list
https://en.wikipedia.org/wiki/Preferential_voting (todo)

https://en.wikipedia.org/wiki/Ranked_voting (todo)


(todo)
(todo)
(todo)
(todo)
(todo)
(todo)
(todo)


## Gain
###### For the dApps
Votes => Exposure

What does exposure mean?
	* a spot in a list (as opposed to relative quantitative gain, as in "Proportional representation")

Interested in all dApps => We want to use ranking

Positive votes (we vote who we want, not who we don't want). The ranking implicitly provites a mechanism to establish who's at the bottom of the food chain (see flagging) 

###### For the users
* Rewards
* Reputation?

## Terminology and fundamental notions 
###### ! differentiate between voting systems and properties of such.
	
want <Ranking>
 Majority (=absolute majority) => Plurality
but want people to not cast only one vote (otherwise we can too few votes).

how to count votes? Especially since there if there are several votes per person, i.e. up to
|users| * |dApps|
votes

######  *) Ranking
==> sign of trust and value
==> dApp producer gets attention

will argue for a form of
https://en.wikipedia.org/wiki/Cardinal_voting
TODO: look at all of those and work out pros and cons and differences.

######  *) Anonymity, Neutrality, Monotonicity
Most fundamental base voting system is majority rule characterized by: 
	- Anonymity (Hodge p.4)
	- Neutrality
	- Monotonicity
	
Facebook likes

- Monotonicity is almost self-evidently valuable. 
- Neutrality is a free market rule. (While nOS has power over the system and can form coalitaitons with individual dApp designers, there is likely no from nOS relizing any sort of bonus in the ranking system. Of course, nOS might promote particular dApps independent of the ranking) 
- Anonymity ... (see Steemit and Anonymity (reputation)
	=> aggregation problem
	=> solition via brakets of last time period
	exposure effect
	
Regading Steemit ... keep an eye on rewards: How it's solved by steemit, complexity, problems.


######  *) Quotas
This is just details: 

In our case, 

1) Quotas <=> Could in principle be used as a cap for when a dApp even enters the ranking. 
On the lower end (i.e. having a low quota) => Could be unfair w.r.t. exposure differences. Being ranked low is enough of a punishment for that.
One could imagine a quota at the ghier end (extra bonus exposue for breaking a benchmark). This can be done with relative numbers, e.g. if the dApps gain a significant fraction of the total votes (see also Required Voting below) or a significat fraction relative to the votes for other dApps (e.g. whenever one dApp gains 110% the number of votes of the dApps below them).

2) Given a computed ranking, quotas <=> Could be used for a hard cap of which apps aren't show on the website

Can be set for when typical numbers (user base, dApp base, size) are established. Such a quote could depend on the website layout or be a running number depending on the number of dApps.
We have a ongoing running voting process with varying user base size and number of dApps.

The majority of dApps should of couse be accessible and searchable on the platform even if they are low in the rank
=> keep an eye on rewards: Steemit system, complications

Both of the above => flagging


######  *) Required voting
Note that majority rule doens't require everybody to vote and this is probably also not something we want to enforce (note on GAS being rewards only when voted). 
This (the lack of fixed number of total votes upfront) makes the design of the decission algorithm harder as it makes benchmarks more volatile, so that previous voting rounds lose predictive content.

######  *) Ties
Due to the large numbers of dApps to be voted for and the high number of voting rounds (and thus low stakes per voting rounds), ties are no real concern for the platform.

######  *) Breaking Neutrality.
While it's not a crucial featues, a tie can easily be deterministically resolved by reflection on timely day, e.g. sign up date (e.g. older or more recent dApps have a bonus) or previous ranking results (e.g. previous winners or non-winners have a bonus). Note that here the finaly ranking would be influenced by the last one.
What makes Neutrality for us different than e.g. for political elections considered in isolation is that we can have a continuous stream of new dApps .
It raises the question of how self-contained a voting round should be in general. An argument for not breaking neutrality (beyond deciding ties) is that it makes process computationally more compact.

One might be tempted to say it also frees us from incoorporating previous data at all. However, below when talking about gamification aspects, which is tied to long term participation and (informal) platform reputation, we'll argue why the past shoud however indeed be involved to compute reward

###### Features for classifications of voting systems

* Plurality voting
* Instant-runoff voting


###### For our consideration

* Reputation ...
* Voting Power ...
* Flag ... dApps can be annotated/singled out for being suspicious/spam 

##### Established voting mechanisms

	


##### Voting system criteria


https://wiki.electorama.com/wiki/Category:Voting_system_criteria
	




## Considerations we want and what we don't want

The voting system should fulfill the following criteria: 

1) User's values: Reputation, Voting Power (reputation and voting power should be dependent, reputation = voting power possible)

2) Reputation grows if user's vote is in consensus with community's votes 
   * a) various ways to predefine what "consensus" does mean
   idea: determine consensus in periods of a week 
   * b)!!! but users should not be able to vote for apps they haven't used only to get rewarded and users should not be motivated to vote for apps only because they already have a high number of votes and therefore are sure to 
   be in consensus
   idea: reward could be higher for the first voters
   idea: votes should cost
   
3) Reputation decreases if user's vote isn't in consenus with communitys's votes

4) bad apps may be reported by users (= some sort of downvoting in very, very bad cases) 

5) the reputation of users should sink whenever their programmed apps get reported

6) if an app has a large number of reports (limit to be predetermined), users should get a warning before downloading and/or running the app

7) apps' values: number of votes, number of reports;
* evaluation based on: 
- a) usage rate (!!! but apps that are needed more often shouldn't have an advantage over apps that are needed rarely)
- b) number of votes
- c) number of reports
- d) time that an app has been in the market
- e) extent of NOS user base

8) user's reward for a consensus vote should not be dependent from user's voting power or reputation (negative model: steemit)

9) reputation and voting power might be limited 
    - a) idea: including a parameter so that at a very high level the increment of reputation converges to 0 

10) data onchain/offchain? 

11) calculation costs

12) for a listed ranking, a dApp should only be added to the average if it has a certain number of votes. This number can be a pecentage of the user base, but shouldn't grow too high (so that new dApps can be added even if the user base is huge)
 
?) Rewards for dApp producers? (If so, it should still probably not depend on raking)

## Discussions of existing voting systems and their pros and cons for our purposes

#### Instant-runoff voting
Issue that well known (old) dApps are far too hard to be taken over

#### xxx

###### Exploration of other platform's (blockchain and centralized ones') voting systems (TODO/WIP): 

    * Lisk voting, earnlisk.com
    * augur "reporting": 50% ROI
    * Gnosis
    * reward voting 7.0
    * openbazaar
    * repu-coin
    * odem.io
    * riskbazaar
    * drep.org
    * stackexchange

## Discussions of existing web platforms and their pros and cons for our purposes
### Blockchain related:
	* Lisk:
	-)delegate proof of stake --> one earns lisk by voting for delegates who share their rewards with their voters (max. number of 		  votes: 101) 
	-)4 batches á max. 33 votes (max. 101 votes at altogether) to participate; 
	-)to participate at a batch, one has to pay 1 lisk, which has to be in the lisk-wallet
	-)(Open question: what happens, if voted delegators don't win --> is the paid lisk just lost?)
	(source: https://earnlisk.com/)
		
### Retailer related:
	* Amazon:
		Ranking factors: (https://startupbros.com/rank-amazon/)
		
		*Conversion Rate Factors:
		- Sales Rank
		- Customer Reviews
		- Answered Questions <--- add as factor to platform highlight algorithm
		- Image Size & Quality
		- Price
		- Parent-Child Products
		- Time on Page & Bounce Rate
		- Product Listing Completeness

		* Relevancy Factors
		- Title
		- Features / Bullet Points
		- Product Description
		- Brand & Manufacturer Part #
		- Specifications
		- Category & Sub-Category
		- Search terms
		- Source Keyword
		
		* Customer Satisfaction & Retention Factors
		- Negative Seller Feedback
		- Order Processing Speed
		- In-Stock Rate
		- Perfect Order Percentage (POP)
		- Order Defect Rate (ODR)
		- Exit Rate
		- Packaging Options
	
	* ebay: 
		+) evaluation of sellers (quite simple): 

		standard evaluation, given by verified buyers:
			-positive vote: + 1 point
			-neutral vote: 0 points
			-negative vote: -1 point
			-one vote per buyer per week (Mon- Sun) is counted 
			-13 different levels of rating of the sellers, symbolized by differently coloured stars

		detailed evaluation, may be given after the standard evaluation: 
			-1-5 stars (voting points) for each of 4 categories (article, communication, sender time, shipping 						costs) possible
			-independent from the standard evaluation, doesn't affect it
			-one rating per purchase possible
			-is are shown only if there are at least 10 detailed evaluations

		+) evaluation of buyers (unimportant for nOS-purposes)
			-buyers can be evaluated by the sellers, but only positive votes are possible

		evaluations can be edited if both parties do agree

		+) evaluation of products: 
			-1-5 stars (5 being the best) 
			-in addition, there are 3 product-specific questions to answer (yes/no) 
			-the average of the stars-rating and the percentage of positive answers to the questions are shown on the product 			   page
			-also, people can write reviews; reviews can be given a positive or negative vote or can be reported
		
		(sources: https://pages.ebay.de/help/feedback/howitworks.html, https://verkaeuferportal.ebay.de/verkaeufer-news/2016-				fruehling/produktbewertungen-rezensionen, https://pages.ebay.de/help/feedback/questions/leave.html)

### Q&A platform related:

xxx
	* StackExchange
	* Quora
	* Reddit
	* News papers
	* ...

### Gaming: 
	*) VotingPlugin 
	(some plugin for Minecraft)
	allows one to give his players rewards by voting for his servers; 
	types of rewards: 
	-) for votes for one site
	-) for voting on all of some specified sites
	-) for the first vote
	-) cummulative reward (vote x amount of times to be rewarded (per day/week)) 
	-) for voting x number of times in a row
	-) for x amount of global votes
	(source: https://www.spigotmc.org/resources/votingplugin.15358/)

TODO: 
* for whitepaper: make USER EXPERIENCE section 
    
################ quick notes, todo: cleanup

## Algorithm details 
### dApp ranking (voting <-)

See file `pseudo-codes.py`

### dApp-producer ranking Algorithm details
Reward for both quality and quantity, and both should be necessary

### Reviews
* Reward for writing reviers, judged on quality

### Rewards

(note: The python file now contains a more elaborate variant of those ideas)

S(n) ... stake of user n 
V(n) ... "how well" they voted
N=sum over n such that n voted right (that will be rewards) ... all users
M ... total reward
x ... fraction of non-stakedependent rewards
R(n) = (x * M) * f(v) + ((1-x) * M) g(n,S(n)) 
	where f(v) says how good they voted, sum over f(v) is 1
	and where g(n,s) depends on the stake  where n-sum over g(n,s) is 1
	
### On-chain requirements

todo: Write a summary of requirements when it comes to storage and script execution

tldr we need 
	* User accounts with a tine by of on-chain data relating to past actons and current users rankings
	* Readout of users ranking, computation of some numbers
	* The result must definately be on-chain, and if the write-back to the user accounts is doable that would be great as well
