#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class node
{
public:
    int data;
    node *left, *right;

    node(int data)
    {
        this->data = data;
        left = right = NULL;
    }
};


int main()
{
int x;
cout<<"Enter the root element :";
cin>>x;
queue<node*> q;
node *root = new node(x);
q.push(root); 
while(!q.empty())
{
    node *temp = q.front();
    q.pop();
    cout<<"\nEnter left child of "<<temp->data<<" :";
    cin>>x;
    if(x != -1)
    {
        temp->left = new node(x);
        q.push(temp->left);
    }

    cout<<"\nEnter right child of "<<temp->data<<" :";
    cin>>x;
    if(x != -1)
    {
        temp->right = new node(x);
        q.push(temp->right);
    }
}


return 0;
}