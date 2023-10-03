#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int choice;
    
    cout << "Choose a shape to calculate the area:" << endl;
    cout << "1. Rectangle" << endl;
    cout << "2. Circle" << endl;
    cout << "3. Triangle" << endl;
    cout << "Enter your choice (1/2/3): ";
    cin >> choice;
    
    switch(choice) {
        case 1: {
            double length, width;
            cout << "Enter the length of the rectangle: ";
            cin >> length;
            cout << "Enter the width of the rectangle: ";
            cin >> width;
            double area = length * width;
            cout << "The area of the rectangle is: " << area << endl;
            break;
        }
        case 2: {
            double radius;
            cout << "Enter the radius of the circle: ";
            cin >> radius;
            double area = M_PI * pow(radius, 2);  // Using pi from the cmath library
            cout << "The area of the circle is: " << area << endl;
            break;
        }
        case 3: {
            double base, height;
            cout << "Enter the base of the triangle: ";
            cin >> base;
            cout << "Enter the height of the triangle: ";
            cin >> height;
            double area = 0.5 * base * height;
            cout << "The area of the triangle is: " << area << endl;
            break;
        }
        default:
            cout << "Invalid choice. Please enter 1, 2, or 3." << endl;
    }
    
    return 0;
}
