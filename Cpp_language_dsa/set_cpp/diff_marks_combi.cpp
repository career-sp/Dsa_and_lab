/*
question: Given the number of questions as n, and marks for the correct answer as p and q marks for the incorrect answer. One can either attempt to solve the question in an examination and get either p marks if the answer is right, or q marks if the answer is wrong, or leave the question unattended and get 0 marks. The task is to find the count of all the different possible marks that one can score in the examination.

input 1: n=2, p=1, q=-1;
output 1: 5;
explanation: the different possible marks are: -2, -1, 0, 1, 2.

time complexity : o(n^2) as we are using nested loop.
space complexity: o(n)

*/

#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

int main()
{
int n,p,q;
cout<<"enter no of values of n, p, q : ";
cin>>n>>p>>q;
cout<<endl;

unordered_set<int> s;

for(int i=0; i<=n; i++)
{
    for(int j=0; j<=n; j++)
    {
        int correct = i;
        int incorrect = j;
        int unattended = n-(i-j);

        if(unattended>=0)
        {
            int score = correct*p + incorrect*q;
            s.insert(score);
        }
        else{
            break;
        }
    }
}

cout<<"possible scores : ";
for(auto value: s)
{
    cout<<value<<" ";
}
cout<<endl;
cout<<"Ans : "<<s.size()<<endl;
}

