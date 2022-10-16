
def reverse_array(arr):
    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

    return arr


def reverse_array_pythonic(arr):
    return arr[::-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(reverse_array(arr))
    print(arr)
    print(reverse_array_pythonic(arr))