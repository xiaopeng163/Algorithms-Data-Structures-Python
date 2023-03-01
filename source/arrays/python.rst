Arrays in Python
=====================

In Python, arrays are called ``lists``. Lists are a very powerful data structure that can be used to store a wide variety of data.
Lists can be used to store numbers, strings, other lists, and even functions. Lists are also very flexible, as they can be resized and their contents can be changed.
Lists are also very easy to use, as they have a wide variety of built-in methods that can be used to manipulate them.

Creating a list
---------------------

To create a list, you simply need to put a comma-separated list of values in square brackets. For example:


    >>> my_list = [1, 2, 3, 4, 5]
    >>> my_list
    [1, 2, 3, 4, 5]


C++ 例子
------------



.. code-block:: c++

    // filename array.cpp
    #include <iostream> // header file for taking input and producing output
    using namespace std;

    int main()
    {
        int arr[4] = {1, 3, 5, 3}; // initializing an array of size 4

        cout << arr[3] << "\n"; // gives the element at index 3
        cout << arr[2] << "\n"; // gives the element at index 2

        return 0;
    }

运行

.. code-block:: bash

    g++ array.cpp
    ./a.out
