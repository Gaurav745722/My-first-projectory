#include<iostream>
using namespace std;
class company
{
    public:
    string company_name;
    string founder_name;    
};
class deprtment:public company
{
    string department_name;
    int noOfEmployee;
    public:
    void input()
    {
        // cout<<"Put the company name: ";
        // cin>>company_name;
        // cout<<"Put the department name: ";
        // cin>>department_name;
        // cout<<"Put the founder name: ";
        // cin>>founder_name;
        company_name="Microsoft";
        department_name="HR department";
        founder_name="Bill gates";
        noOfEmployee=948393043;
    }
    void display()
    {
        cout<<"company name: "<<company_name<<"\n Founder name: "<<founder_name<<"\n Department name: "<<department_name<<"\nNo. of employee: "<<noOfEmployee<<endl;
    }
};
main()
{
    deprtment d;
    d.input();
    d.display();
}