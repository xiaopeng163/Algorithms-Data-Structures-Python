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
        i + 1

    while j < len(l2):
        result.append(l2[j])
        j += 1
    return result


result = merge([1, 3, 5, 6], [2, 4, 7, 8])
print(result)
