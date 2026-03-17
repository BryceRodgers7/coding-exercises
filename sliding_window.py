# Question 1
# Find the maximum sum of a subarray of size k.
# nums = [2,1,5,1,3,2]
# k=3








































def max_sum_subarray(nums, k):
    # calculate sum of first k elements, then scan thru adding next & removing previous
    
    if k <= 0 or len(nums) < k:
        return None
    
    current_sum = sum(nums[:k])
    result = current_sum

    for i in range(len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if (current_sum > result):
            result = current_sum

    return result

def max_sum_sub2(nums, k):
    # scan thru, adding next num & subtracting previous num
    if k <= 0 or len(nums) < k:
        return None
    
    left = 0
    right = k
    sum = sum(nums[:right])
    max = sum

    for i in range(1, len(nums) - k + 1):
        sum += nums[right]
        sum -= nums[left]
        right +=1
        left += 1
        if sum > max:
            max = sum
    return max

def biggest_subarr(nums, k):
    # scan thru ~length-k windows, keep a running total
    if k <= 0 or k > len(nums):
        return None
    
    t = None
    for i in range(len(nums) - k + 1):
        s = 0
        for j in range(i, i + k):
            s += nums[j]
        if t == None or s > t :
            t = s
    return t


# BETTER ANSWER:
def biggest_subarr_btr(nums, k):
    # calc first window
    # cycle thru/check all windows, adding the new element & removing the last one
    if k <= 0 or k > len(nums):
        return None
    current_window = sum(nums[:k])
    max_window = current_window

    for i in range (len(nums) - k):
        current_window += nums[i + k]
        current_window -= nums[i]

        if current_window > max_window:
            max_window = current_window
    return max_window



# Question 2
# Find the length of the longest substring without repeating characters.
# Example:
# "abcabcbb" → 3





































def longest_substr(s):
    # keep track of seen characters with a set
    # scan right until a character is seen, shrink from left until its not-seen

    if not s or len(s) < 1:
        return None

    seen = set()
    left = result = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])            

        if len(seen) > result:
            result = len(seen)

    return result

def longest_nonrep_substr(s):
    # scan thru, keeping set of seen chars
    # if next/right char is seen, keep removing last/left char until not seen
    if not s or len(s) < 1:
        return None
    seen = set()
    left = 0
    max_len = 1

    for i in range(len(s)):

        while s[i] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[i])

        if len(seen) > max_len:
            max_len = len(seen)

    return max_len

def longest_substring(s):
    # check a window of changing size, starting from the left
    # if next char is not unique, shrink from left until it is, then grow right

    seen = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        if len(seen) > longest:
            longest = len(seen)
    return longest