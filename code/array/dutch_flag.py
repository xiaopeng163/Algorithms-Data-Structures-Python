def dutch_flag_problem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:

        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] > pivot:
            nums[j], nums[k] = nums[k], nums[j]
            k = k - 1

        else:
            j += 1
    return nums

if __name__ == '__main__':

    nums = [1, 0, 2, 2, 1, 0, 0, 2, 1]
    print(dutch_flag_problem(nums, 1))