# Question 1
# Given a sorted array and a target sum, return the indices of two numbers that add up to the target.
# nums=[1,2,4,6,10]
# target=8

# REMEMBER, ITS SORTED!!










































def get_sum_indicies(nums, target):
    # scan inwards summing both ends, if target > current_sum move up from left, else move down from right
    if not nums or len(nums) < 2:
        return None
    
    left = 0
    right = len(nums) - 1
    current_sum = 0

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else: # current_sum > target
            right -= 1
    
    return None

def sum_index(arr, target):
    # scan inwards from both ends, moving one side or the other based on > or < target
    if len(arr) < 1:
        return None
    
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return left, right
        elif sum > target:
            right -= 1
        else: # sum < target
            left += 1
    
    return None


def target_index(arr, target):
    # scan inward from both ends
    # if target is larger, move left
    # if smaller move right
    if len(arr) < 1:
        return None
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if (sum == target):
            return left, right
        elif (sum < target):
            left += 1
        else: # sum > target
            right -= 1
    return None

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
def is_palindrome(s):
    # scan inwards from both ends, looking for any chars that do not match
    s = re.sub('^a-zA-Z0-9', '', s).lower()

    if len(s) == 0:
        return False

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
        
    return True


import re
def is_palindrome(s):
    # scan inwards looking for chars that do not match
    s = re.sub('^a-zA-Z0-9', '', s).lower()

    if len(s) == 0:
        return False

    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

import re
def is_palindrome3(s):
    # scan from both ends, checking if any chars mismatch
    s = re.sub('^a-zA-Z0-9', '', s).lower()

    if len(s) == 0:
        return False

    for i in range(len(s) // 2):
        if (s[i] != s[len(s) - i - 1]):
            return False
    return True

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
