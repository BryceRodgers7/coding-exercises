# 1
# Given an array of integers, return the element that appears most frequently.
# Example:
# Input: [1,3,2,3,4,3,5]
# Output: 3




































from collections import Counter
def most_freq(arr):
    # use Counter from collections, get key with highest value
    counts = Counter(arr)
    return max(counts, key = counts.get)

from collections import Counter
def most_frequent(nums):
    # create hash, get key with largest value
    counts = Counter(nums)
    return max(counts, key=counts.get)


from collections import Counter
def most_freq(arr):
    # use Counters hash, return key with max value
    counts = Counter(arr)
    return max(counts, key=counts.get)

from collections import Counter
def most_freq(arr):
    # scan thru, create hash of counts for each value

    counts = Counter(arr)
    return max(counts, key=counts.get)

from collections import Counter
def most_frequent2(arr):
    counts = Counter(arr)
    return max(counts, key=counts.get)

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
    # use Counter to check if char count matches
    return Counter(s) == Counter(t)

from collections import Counter
def is_anagram(s, t):
    # check if Counter hash is the same for both strings
    return Counter(s) == Counter(t)

from collections import Counter
def is_anagram(s, t):
    # check if Counter objects match
    return Counter(s) == Counter(t)

from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)

from collections import Counter
def is_anagram(s, t):
    # check the count of each letter in both strings
    return Counter(s) == Counter(t)

from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)
























# answer: use Counter again
def is_anagram(s, t):
    from collections import Counter
    return Counter(s) == Counter(t)




