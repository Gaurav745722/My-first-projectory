#include<iostream>
using namespace std;
int main()
{
    string s;
    cout<<"Enter the string: ";
    cin>>s;
    //pre compute
    int hash[26]={0};
    for(int i=0;i<s.size();i++)
    {
        hash[s[i]]++;
    }
    int q;
    cout<<"\n Enter number how many times to check: ";
    cin>>q;
    while(q--)
    {
        char c;
        cout<<"\nEnter what you check: ";
        cin>>c;
        //fetch
        cout<<hash[c]<<endl;
    }
    return 0 ;
}