#include<iostream>
using namespace std;
void printpattern_1(int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=i;j<n;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
    cout<<endl;
}

void printpattern_2(int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<=i;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
    cout<<endl;
}
void printpattern_3(int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=n;j>=0;j--)
        {
            if(j==i)
            cout<<"*";
        }
        cout<<endl;
    }
    cout<<endl;
}
main()
{
    int n;
    cout<<"\nEnter the any number: ";
    cin>>n;
    printpattern_1(n);
    printpattern_2(n);
    printpattern_3(n);
}