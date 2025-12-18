#include<iostream>
using namespace std;
int fun(int n)
{
    if(n<0)
    return 1;
    cout<<"\n*\t";
    fun(n-1);
}
main()
{
    int n;
    cout<<"\nEnter any number: ";
    cin>>n;
    fun(n);
}