#include <iostream> // header file for taking input and producing output
using namespace std;

int main()
{
	int array[4] = {1, 3, 5, 7}; // initializing an array of size 4
	int *ptr;										 // declaring a pointer

	cout << array[3] << "\n"; // gives the element at index 3
	cout << array[2] << "\n"; // gives the element at index 2

	cout << "==================================================\n";
	cout << "Displaying the Address of The Pointer of an Array";
	cout << "\n=================================================\n\n";

	int i;
	for (i = 0; i < 4; i++)
	{
		cout << "Address Of " << array[i] << " Using Array is ===> " << &array[i] << endl;
	}

	cout << "\n========================================\n";
	return 0;
}