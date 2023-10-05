#include<iostream>
using namespace std;
int main()
{
    int n;

    cout << "enter the value of n : " << endl;
    cin >> n;

    int i = 2; // 2 because 1 is divisible by every number 

    while (i < n)
    {
        if (n % i == 0)
        {
            cout << "The number is not prime for : " << i <<  endl;
        }
        else
        {
            cout << "The number is prime for : " << i << endl;
        }
        i = i + 1;
        
    }
    
    return 0;
}
