# Question 1
# Given a sorted array and a target sum, return the indices of two numbers that add up to the target.
# nums=[1,2,4,6,10]
# target=8

# REMEMBER, ITS SORTED!!














def target_sum2(nums, target):
    # sorted means we can start from the edges and work our way inwards
    # if outer sum is too small, move in from right
    # if outer sum is too large, move in from left
    if len(nums) < 2:
        return None
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return left, right
        elif sum < target:
            left +=1
        elif sum > target:
            right -=1

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
def is_palindrome2(s):
    # scan inwards from both ends, checking if letters match
    s = re.sub('^a-zA-Z0-9', '', s).lower()
    if len(s) == 0:
        return False
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
    
import re
def is_palindrome(s):
    s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    # scan from both ends checking if each char is equivalent
    for i in range (len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
