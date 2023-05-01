def pivot(my_list):

    pivot_index = 0
    swap_index = 0
    swap = False

    for i in range(pivot_index + 1, len(my_list)):

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


my_list = [6, 5, 3, 1, 8, 7, 2, 4]
pivot(my_list)
print(my_list)
