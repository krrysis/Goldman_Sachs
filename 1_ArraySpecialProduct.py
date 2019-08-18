"""

Array Special Product

Implement a function which, given an array of integers, returns a new array for which every index carries the value of the product of the remaining elements.

 

Example

Given array [1, 3, 2, 4, 5] it would return [120, 40, 60, 30, 24]

Given array [4, 10, 3] it would return [30, 12, 40]

 

Function Description

The function findSpecialProduct accepts the following parameters

- An array of integers "input" of size n.

The function must return a new array of size n in which every index carries the value of the product of the remaining elements.

 

Input Format

n                                             # 1st line specifies the number of elements on the array

in[1]                                        # Next n lines has a list of integers.

in[2]

..

in[n]           

 

Output Format

out[1]                                      # output has an array of n integers with each integer in a line.

out[2]

…

out[n]   

 

Constraints

 

Division operator cannot be used.

Expected time complexity is strictly O(n)

0 <= n <= 5

0 <= in[i] <= 10;  0 <= i < n

 

Sample Input values

5

1

2

3

4

5

 

Sample Output values

120

60

40

30

24

"""



n=int(input("Enter the number of elements in an array"))
input_array=[]
output_array=[]
for x in range(0,n):
    input_array.append(input('enter next element'))
prod=1
for y in range(0,n):
    for z in range(0,n):
        if(z!=y):
            prod*=int(input_array[z])
            
    output_array.append(prod)
    prod=1

print(output_array)
