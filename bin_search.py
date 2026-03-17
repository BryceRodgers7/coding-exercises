# Question 1
# Find the index of target in a sorted array.



































def find_target(arr, target):
    # calculate mid-point for min/max possible index and check
    left = 0
    right = len(arr)-1

    while left <= right:
        m = ( right + left ) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            right = m - 1
        else: #arr[m] < target
            left = m + 1
    return -1




# Question 2

# Find the first occurrence of a number in a sorted array.




































def first_occur(arr, target):
    # calculate mid-point for min/max possible index and check
    # after found, scan left 
    left = 0
    right = len(arr)-1

    while left <= right:
        m = ( right + left ) // 2
        if arr[m] == target:
            while m >= 0:
                if m == 0:
                    if arr[m] == target:
                        return 0
                    else:
                        return 1
                m -= 1
                if arr[m] != target:
                    return m + 1
        elif arr[m] > target:
            right = m - 1
        else: #arr[m] < target
            left = m + 1
    return -1

# or just reduce right by 1 even when arr[m] == target  OR  change the m-1 logic to >= from strictly >