"""
Subsets of 0s

Ashutosh is a very mischievous student. His mathematics teacher wants to teach him a lesson so, he gave Ashutosh an array of positive integers Arr[a1, a2,....,an] where ai>0. primeSum is an integer which is equal to sum of all the prime factors of each element in Arr, modulus (10^6). Ashutosh's job is to find no of ways in which a set of 'primeSum' number of 0s can be divided into k subsets modulus(10^9+7).

Ashutosh is a little nervous, can you help him get out of this trouble ?

Note: A subset can be empty

 

INPUT:

The first line indicates the number of subsets, k.
The next line has a single integer n denoting the length of array.
Next n lines contain the integers in the array.
 

Input Format for custom testing:

2 --> number of subsets, k

3 --> length of the array

3 --> length of the array for hackerrank representation of integer array followed by  elements of the array
1 
2
6
 

OUTPUT:
An integer representing the number of ways in which a set of primeSum number of 0s can be divided into k subsets mod (10^9+7).

 

Constraints:
0<ai<=10^6
1<=n<=10^5
1<=k<=100

 

Sample:

 

INPUT:

2

3

3
1
2
6

 

OUTPUT:

8

 

EXPLANATION:

The sum of all prime factors of elements of array modulus 10^6 is 7 
A set of 7 0s can be divided into 2 subsets in 8 different ways. - {{}, {0, 0, 0, 0, 0, 0 ,0}}, {{0}, {0, 0, 0, 0, 0 ,0}}, {{0, 0}, {0, 0, 0, 0 ,0}} and so on.

So answer is 8 modulus 10^9+7 = 8.

 

INPUT:

3

3

3
1
2
6

 

OUTPUT:

36

 

EXPLANATION:

The sum of all prime factors of elements of array modulus 10^6 is 7 
A set of 7 0s can be divided into 3 subsets in 36 different ways.
So answer is 36 modulus 10^9+7 = 36.
"""
