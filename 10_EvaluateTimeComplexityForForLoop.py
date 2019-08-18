"""
10_Evaluate Time complexity for For loop

int fun(int n){
    int count=0;
    for(int i = n;i>0; i/=2)
        for(int j=0; j < i ; j++)
            count += 1;
    return count;
} 

What is the run time complexity of the above code?
Pick one of the choices

    O(n2)

    O(n log n)

    O(n)

    O(n log(log n))

    None of the above
"""