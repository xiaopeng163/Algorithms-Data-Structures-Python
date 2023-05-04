def pivot(my_list, start_index, end_index):

    pivot_index = start_index
    swap_index = pivot_index
    swap = False

    for i in range(pivot_index + 1, end_index + 1):

        if my_list[i] < my_list[pivot_index]:

            if swap:
                swap_index += 1
                my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]
            else:
                swap_index += 1
            i += 1

        elif my_list[i] > my_list[pivot_index]:
            i += 1
            swap = True

    my_list[pivot_index], my_list[swap_index] = (
        my_list[swap_index],
        my_list[pivot_index],
    )

    return swap_index


my_list = [6, 5, 3, 1, 8, 7, 2, 4]


def quick_sort(my_list, start_index, end_index):

    if start_index < end_index:

        pivot_index = pivot(my_list, start_index, end_index)

        quick_sort(my_list, start_index, pivot_index)
        quick_sort(my_list, pivot_index + 1, end_index)


quick_sort(my_list, 0, len(my_list) - 1)

print(my_list)
