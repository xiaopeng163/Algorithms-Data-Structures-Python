def bubble_sort(array):

    n = len(array)

    for i in range(n):

        for j in range(0, n - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = [5, 1, 4, 2, 8]
bubble_sort(array=array)

print(array)
