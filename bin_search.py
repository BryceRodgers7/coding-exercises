# Question 1
# Find the index of target in a sorted array.
# arr = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   target = 7





































def find_target_index(nums, target):
    # repeatedly check midpoint, then exclude the half of the sorted array it cannot be in
    if not nums or len(nums) < 1:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            left = m + 1
        else: # nums[m] > target
            right = m - 1
    return -1

def find_trgt(arr, target):
    # check middle, look half-way to the right or left if larger/smaller
    if not arr or len(arr) < 1:
        return None
    left = 0
    right = len(arr) - 1

    while left <= right:
        m = (right + left) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            left = m + 1
        else: # arr[m] > target
            right = m - 1
    return None


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
# arr = [1, 1, 2, 2, 2, 2, 3, 4, 5, 6]   target = 2








































def first_occur(nums, target):
    # repeatedly check midpoint, then eliminate half 
    # once found, scan left until no match
    
    result = -1
    if not nums or len(nums) < 1:
        return result

    left = 0
    right = len(nums) - 1
    
    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            result = m 
            right = m - 1
        elif nums[m] < target:
            left = m + 1
        else: # nums[m] > target
            right = m - 1
    return result


def first_occur(arr, target):
    # check if midpoint matches target, if not shrink from left or right depending if > or <
    # if matches, scan left until value changes
    if not arr or len(arr) < 1:
        return None
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        m = (left + right) // 2
        if arr[m] == target:
            result = m 
            right = m - 1
        elif arr[m] > target:
            right = m - 1
        else: # arr[m] < target
            left = m + 1

    return result



def first_occur(arr, target):
    # check if midpoint matches target, if not shrink from left or right depending if > or <
    # if matches, scan left until value changes
    if not arr or len(arr) < 1:
        return None
    left = 0
    right = len(arr) - 1

    while left <= right:
        m = (left + right) // 2
        if arr[m] == target:
            # scan left as long as arr[m] == target
            while m > 0 and arr[m - 1] == target:
                m -= 1
                
            return m

        elif arr[m] > target:
            right = m - 1
        else: # arr[m] < target
            left = m + 1

    return None

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