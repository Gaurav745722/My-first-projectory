#include<iostream>
using namespace std;

class single {
private:
    int x;
    int y;
    int m;
    int n;
public:
    // Default constructor
    single() {
        x = 56;
        y = 45;
    }

    // Parameterized constructor
    single(int a, int b) {
        x = a;
        y = b;
    }

    // Copy constructor
    single(const single &s) {
        m = s.x;
        n = s.y;
    }

    // Destructor
    ~single() {}

    // Display function
    inline void display() {
        cout << "x= " << x << "    y= " << y << endl;
    }
};

int main() {
    single z, f;
    cout << "Default constructor\n";
    z.display();

    cout << "Parameterized constructor\n";
    single x(34*4, 34 / 2);
    x.display();

    cout << "Copy constructor\n";
    single m(2 + 22 / 3, 54);
    f.display();

    return 0;
}
