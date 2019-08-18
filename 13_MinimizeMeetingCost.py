"""
13_Minimize meeting cost

GS has hired Harsh, Rahul, Ankita and Niranjan who happen to be childhood friends. They have been sent to a new city for the onboarding process.
GS has given them a choice to choose any hotel in this city.

This city unlike other cities is a matrix of hotels and there are no roads. If any of the friends go through a hotel even once, the group will have to pay its full rent. From a hotel, you can go to the hotels to its North, South, East, or West.

Since Harsh, Rahul, Ankita and Niranjan are childhood buddies, they want to meet each other. Strangely enough, all four are very particular about the direction they travel so Harsh only goes West, Rahul only goes North, Ankita only goes East, and Niranjan only goes South.

Any number of friends can live in any of the hotels. Living Cost of all the hotels in the city are given, some of which may be negative. Negative cost means if any of the friends lives in or goes through this hotel, the group will get paid an amount equal to the negation of the cost. Now the aim of the four friends is to find the minimum cost for all of them to meet at a particular hotel.


Input

First line contains an integer N denoting the number of rows in the matrix

Second line contains an integer M denoting the number of columns in the matrix.

Next N lines describe the rows of the matrix follow, one row per line. Each row contains M space-separated integers denoting the cost of the hotel.

Output
Output the minimum cost.

Constraints

1 ≤ N ≤ 10^3
1 ≤ M ≤ 10^3
-10^4 ≤ Cost of any apartment ≤ 10^4

Examples:

Input:
3

3
1 2 3
4 -10 5
6 7 8

Output:
-10
 

Explanation:

Harsh, Rahul, Ankita and Niranjan can choose any hotel.

If they choose the following:

Harsh      – [1, 2] where [i, j] represents the indices in the matrix (0 based indexing)

Rahul      – [2, 1]

Ankita     – [1, 0]

Niranjan – [0, 1]

 

Harsh only goes West, Rahul only goes North, Ankita only goes East and Niranjan only goes South, so they can meet at [1, 1].

 

The cost incurred to the group = 4 + -10 + 5 + 2 + 7 = 8

1
	

2
	

3

4
	

-10
	

5

6
	

7
	

8

 

Similarly, the optimum positions is when all the 4 friends are in [1, 1]. Total cost incurred = -10.
"""