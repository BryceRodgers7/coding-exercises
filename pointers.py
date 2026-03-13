# Question 1
# Given a sorted array and a target sum, return the indices of two numbers that add up to the target.
# nums=[1,2,4,6,10]
# target=8

# wrong answer
def target_sum(nums, target):
    # scan thru adding current position to every other position
    if len(nums) < 2:
        return None
    for i in range(len(nums)-1):
        for j in range (i + 1, len(nums)-1):
            if (nums[i] + nums[len(nums)-j-1]) == target:
                return i, j
    return None

# correct answer
def sum_target(nums, target):
    # scan from both ends (because sorted) checking if sum is > or < target, update left/right accordingly
    left = 0
    right = len(nums)-1

    while left < right:
        s = nums[left] + nums[right]

        if (s == target):
            return [left, right]
        elif (s < target):
            right -+ 1
        else: # s > target
            left += 1
    return None            




# Question 2
# Determine if a string is a palindrome, ignoring non-alphanumeric characters.
# "A man, a plan, a canal: Panama"

import re
def is_palindrome(s):
    s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    # scan from both ends checking if each char is equivalent
    for i in range (len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
