def merge(l1, l2):
    # merge to sorted list
    result = []
    i = j = 0

    while i < len(l1) and j < len(l2):

        if l1[i] > l2[j]:
            result.append(l2[j])
            j += 1
        elif l1[i] < l2[j]:
            result.append(l1[i])
            i += 1

    while i < len(l1):
        result.append(l1[i])
        i += 1

    while j < len(l2):
        result.append(l2[j])
        j += 1
    return result


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


result = merge_sort([6, 5, 3, 1, 8, 7, 2, 4])
print(result)
