#include<iostream>
using namespace std;
class college 
{
    public:
    string college_name;
    string college_code;
};
class course
{
    public:
    string course_name;
};
class student :public college,course
{
    string student_name;
    double roll_no;
    public: 
    void getdata()
    {
        college::college_name="United institute of management.";
        college_code="PRSU23073202";
        course_name="Bachlor of computer engineer(BCA)";
        student_name="gaurav kumar";
        roll_no=2412105201131;
    }
    void display()
    {
        cout<<"\n";
        cout<<"\t\t\t\t"<<college_name<<"\n";
        cout<<"\t\t\t"<<college_code<<"\n";
        cout<<"\t\t\t"<<course_name<<"\n";
        cout<<"\t\t\t"<<student_name<<"\n";
        cout<<"\t\t\t"<<roll_no<<endl;
    }
};
main()
{
    student s;
    //s.display();
    s.getdata();
    s.display();
}