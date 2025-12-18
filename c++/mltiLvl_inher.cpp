#include<iostream>
using namespace std;
class car
{
    protected:
    string carName;
    string carType;
    string speed;
    int sitCapacity;  
};
class electricCar : public car
{

};
class petrolCar : public electricCar
{

};
class CNGcar : public petrolCar
{
    public:
    void input()
    {
        carName="Farari";
        carType="Sports car";
        speed="0-480";
        sitCapacity=02;
    }
    void display()
    {
        cout<<"____________________ ___________________________________________________________________\n";
        cout<<"|\t\t\t\t Multilevel Inheritence \t\t\t\t|\n";
        cout<<"|\t\t\t_________________________________________\t\t\t|\n";
        cout<<"|\t\t\t|\t\t"<<carName<<"\t\t\t|\t\t\t|\n";
        cout<<"|\t\t\t|\t\t"<<carType<<"\t\t|\t\t\t|\n";
        cout<<"|\t\t\t|\t\t"<<speed<<" speed"<<"\t\t|\t\t\t|\n";
        cout<<"|\t\t\t|\t\t"<<sitCapacity<<" sit\t\t\t|\t\t\t|\n";
        cout<<"|\t\t\t_________________________________________\t\t\t|\n";
        cout<<"_______________________________________________________________________________________\n\n\n";
    }
};
main()
{
    CNGcar tata;
    tata.input();
    tata.display();
}