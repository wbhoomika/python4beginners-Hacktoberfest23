#include <iostream>
using namespace std;

int main()
{

  bool check = true;

  while (check)
  {
    char op;
    float num1, num2;
    cout << "\n\nEnter operator: +, -, *, / \nto exit enter: z\n::- ";
    cin >> op;
    if (op != 'z')
    {
      cout << "Enter two operands: ";
      cin >> num1 >> num2;
    }
    switch (op)
    {

    case '+':
      cout << num1 << " + " << num2 << " = " << num1 + num2;
      break;

    case '-':
      cout << num1 << " - " << num2 << " = " << num1 - num2;
      break;

    case '*':
      cout << num1 << " * " << num2 << " = " << num1 * num2;
      break;

    case '/':
      cout << num1 << " / " << num2 << " = " << num1 / num2;
      break;
    case 'z':
      check = false;
      break;
    default:
      // If the operator is other than +, -, * or /, error message is shown
      cout << "Error! operator is not correct";
      break;
    }
  }
  cout << "THANK YOU FOR USING CALCULATOR" << endl;
  return 0;
}