def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:

            arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [5, 1, 4, 2, 8]
selection_sort(arr)

print(arr)
