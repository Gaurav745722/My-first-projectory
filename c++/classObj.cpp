#include<iostream> 
using namespace std;
class demo //demo is a class
{
    public:            //public is access specifire
    string name;      // name ,age, roll, marks is class (demo) member
    int age; 
    double roll;
    float marks;
    
};
 main()
{
    demo d;     //d is demo class object, use to access all member variable
    cout<<"Enter the name ,age ,roll and marks: ";
    cin>>d.name>>d.age>>d.roll>>d.marks;
    cout<<"Name: "<<d.name<<"\n Age: "<<d.age<<"\n RollNo: "<<d.roll<<"\n Marks: "<<d.marks;
}
