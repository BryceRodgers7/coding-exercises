# 1
# Given an array of integers, return the element that appears most frequently.
# Example:
# Input: [1,3,2,3,4,3,5]
# Output: 3

def most_frequent(arr):
    # create array where position = num in the input array
    # increment value in position as you see the number
    # return largest number in the array
    counts = []
    for x in arr:
        if counts[x]:
            counts[x]+=1
        else:
            counts[x] = 1
    max = 0
    for c in counts:
        if c > max:
            max = c
    return max

# answer: use Counter from collections
from collections import Counter
def most_frequent(nums):
    counts = Counter(nums)
    return max(counts, key=counts.get)





# 2
# Given two strings s and t, determine if t is an anagram of s.
# Example:
# Input: s="listen", t="silent"
# Output: True


from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)
























# answer: use Counter again
def is_anagram(s, t):
    from collections import Counter
    return Counter(s) == Counter(t)




