#include<iostream>
using namespace std;
int hasing(int arr[],int n,int num)
{
    int i,count=0;
    for(i=0;i<n;i++)
    {
        if(arr[i]==num)
        count++;
    }
    return count;
}
main()
{
    int temp,num,arr[]={1,2,3,4,5,6,7,8,9,6,3,2,6,1,4,4,4,4,2,3,1,6,4,2,8,5,3,8,7,5,2,7,8,5};
    cout<<"1,2,3,4,5,6,7,8,9,6,3,2,6,1,4,4,4,4,2,3,1,6,4,2,8,5,3,8,7,5,2,7,8,5";
    int n=sizeof(arr)/sizeof(arr[0]);
    cout<<"\nEnter the No. you want to check how many times present in given digits: ";
    cin>>num;
    temp=hasing(arr,n,num);
    if(temp==0)
    cout<<"Does't present";
    else
    cout<<temp<<"times present.";
}