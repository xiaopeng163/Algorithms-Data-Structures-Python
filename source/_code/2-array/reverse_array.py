from typing import List


def reverse_array(arr: List) -> List:
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


def reverse_array_pythonic(arr: List) -> List:

    return arr[::-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(reverse_array(arr))
    print(arr)

    print(reverse_array_pythonic(arr))
