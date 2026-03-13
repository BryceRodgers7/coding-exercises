# Question 1
# Find the maximum sum of a subarray of size k.
# nums = [2,1,5,1,3,2]
# k=3

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