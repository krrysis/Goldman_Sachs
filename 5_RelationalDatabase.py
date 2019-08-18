"""
5_RelationalDatabase

A relational database contains two tables PersonDetails and MovieWatched as shown below:

 

PersonDetails:
ID 	Name 	Age
1 	Samyra 	8
2 	Tanvi 	12
3 	Vinay 	28
4 	Prasad 	42
5 	Shanu 	53

 

 

MovieWatched
ID 	Language 	NumberOfMovies
2 	Hindi 	10
2 	English 	25
3 	French 	3
5 	English 	35
5 	Spanish 	10
5 	Hindi 	20

 

 

The Primary key of the PersonDetails table is ID. For MovieWatched ID and Language together form the primary key. Consider the SQL query given below:

 

SELECT P.Name , sum(M.NumberOfMovies)

FROM PersonDetails P, MovieWatched M

WHERE M.NumberOfMovies > 5

GROUP BY P.Name;

 

How many number of rows will the above query return?

 
Pick one of the choices

    2
    3
    4
    5
    none of the above

ANSWER: 2
"""
