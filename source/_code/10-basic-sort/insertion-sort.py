def insertion_sort(arr):

    for i in range(1, len(arr)):

        current_value = arr[i]
        position = i

        while position > 0 and current_value < arr[position - 1]:

            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

    return arr


arr = [5, 1, 4, 2, 8]
insertion_sort(arr=arr)
print(arr)
