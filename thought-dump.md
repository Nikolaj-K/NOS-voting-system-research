### Considerations: 
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
   
Exploration of other platform's (blockchain and centralized ones') voting systems (TODO/WIP): 

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
    
    
################ quick notes, todo: cleanup



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
