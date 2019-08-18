"""
12_Adjacency matrix

Given the following program, what will be the 4th number that’d get printed in the output sequence for the given input?

 

#include <bits/stdc++.h> 
using namespace std; 
int cur=0; 
int matrix[12][12]; 
bool visited[12]; 
deque <int> queue; 
 
void function(int n); 
 
int main()
{   
    int num=0; 
    int n; 
    cin>>n; 
 
    for(int i=0;i<n;i++) 
          for(int j=0;j<n;j++) 
            cin>>matrix[i][j]; 
 
    for(int i=0;i<n;i++) 
        visited[i]=false; 
 
        function(n); 
    return 0; 
} 
 
void function(int n)
{ 
    cout<<cur<<" "; 
    visited[cur]=true; 
    queue.push_back(cur); 
 
    do
        { 
        for(int j=0;j<n;j++)
                { 
            if(matrix[cur][j]==1 && !visited[j])
                    { 
                queue.push_back(j); 
                cout<<j<<" "; 
                visited[j]=true; 
                } 
 
                 } 
 
        queue.pop_front(); 
        if(!queue.empty()) 
        cur=queue.front(); 
     }while(!queue.empty()); 
}

Input Sequence - 

11 
0 0 0 1 0 0 0 0 0    
0 1 0 0 0 0 0 0 1 
0 0 1 1 1 0 0 0 1 
0 0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 1 0 
0 1 1 0 0 0 1 0 1 
0 0 0 1 0 0 0 1 0 
1 0 0 0 1 0 1 0 0 
1 0 1 0 0 0 1 0 0
0 1 0 0 1 0 1 0 1
0 0 0 0 1 0 0 0 0
Pick one of the choices

    2
    6
    8
    5
    None of the above
Adjacency matrix

Given the following program, what will be the 4th number that’d get printed in the output sequence for the given input?

 

#include <bits/stdc++.h> 
using namespace std; 
int cur=0; 
int matrix[12][12]; 
bool visited[12]; 
deque <int> queue; 
 
void function(int n); 
 
int main()
{   
    int num=0; 
    int n; 
    cin>>n; 
 
    for(int i=0;i<n;i++) 
          for(int j=0;j<n;j++) 
            cin>>matrix[i][j]; 
 
    for(int i=0;i<n;i++) 
        visited[i]=false; 
 
        function(n); 
    return 0; 
} 
 
void function(int n)
{ 
    cout<<cur<<" "; 
    visited[cur]=true; 
    queue.push_back(cur); 
 
    do
        { 
        for(int j=0;j<n;j++)
                { 
            if(matrix[cur][j]==1 && !visited[j])
                    { 
                queue.push_back(j); 
                cout<<j<<" "; 
                visited[j]=true; 
                } 
 
                 } 
 
        queue.pop_front(); 
        if(!queue.empty()) 
        cur=queue.front(); 
     }while(!queue.empty()); 
}

Input Sequence - 

11 
0 0 0 1 0 0 0 0 0    
0 1 0 0 0 0 0 0 1 
0 0 1 1 1 0 0 0 1 
0 0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 1 0 
0 1 1 0 0 0 1 0 1 
0 0 0 1 0 0 0 1 0 
1 0 0 0 1 0 1 0 0 
1 0 1 0 0 0 1 0 0
0 1 0 0 1 0 1 0 1
0 0 0 0 1 0 0 0 0
Pick one of the choices

    2
    6
    8
    5
    None of the above
"""