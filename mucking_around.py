# Practice evaluating AI-generated code:



# Write a Python function first_unique_char(s) that returns the index of the first non-repeating character in a string, or -1 if every character repeats.

# example input string:  s = "abcbcd"  or   s = "aaabcda"

def first_unique_char(s):
    counts = {}
    for ch in s:
        counts[ch] = 1

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

# this solution is partially correct, it does correctly return the index of the first non-repeating char, but it will incorrectly return -1 for an empty string, or a string of length 1.
# The requirements do not include the expected outcome for an empty string, because there are no repeating or non-repeating characters. 
# The complexity for runtime is O(2n) with extra space O(n), but an optimal solution runs in O(n) time extra space O(1).

# optimal answer:

def first_unique_char(s):
    if len(s) == 0:
        return None
    if len(s) == 1:
        return 0

    for i, ch in enumerate(s):
        if ch != s[0]:
            return i
    return -1

# WRONG!!!!! repeating is based on char-frequency, not seeing it again while scanning through it.




# Write a Python function longest_substring_no_repeat(s) that returns the length of the longest substring without repeating characters.

def longest_substring_no_repeat(s):
    seen = set()
    max_length = 0

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            max_length = max(max_length, len(seen))
        else:
            seen.clear()
            seen.add(ch)

    return max_length



# This is incorrect, the moment it sees a repeating character it starts over, so it will miss longer substrings when the repeating character was at the start of the substring.
# What it should do is shrink the substring from the left until the seen character is no longer included, the continue growing to the right until it encounters another seen char or the end of the string.
# Its complexity is O(n) time with extra space O(n) but an optimal solution would run in O(n^2) time with extra space O(n)"

def longest_substring_no_repeat(s):
    seen = set()
    max_length = 0
    left = 0

    for right in range(len(s)):
        while left <= right:
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
        seen.add(s[right])
        max_length = max(max_length, len(seen))

    return max_length


# slightly wrong, still O(n) time, and while condition should be 's[right] in seen'







# Write a Python function merge_sorted(a, b) that merges two sorted lists into one sorted list.

def merge_sorted(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    return result + a[i:] + b[j:]

# the answer is partially correct, but it has a bug, it will throw an index out-of-bounds error at the end with either a[i:] or b[j:]
# the correct answer is to check which array's elements were not yet added to the result, and only add those remaining elements to the end
# the complexity of the answer is O(n) time with O(n) extra space and the correct answer also has O(n) time with O(n) extra space

# sample inputs a = [1, 2, 6, 9, 10, 10, 10]  b = [1, 1, 2, 3, 5, 7, 9, 10]

def merge_sorted(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else: # a[i] >= b[j]
            result.append(b[j])
            j += 1

    if j < len(b):
        remaining = b[j:]
    else: # i < len(a)
        remaining = a[i:]

    return result + remaining

# wrong again (slightly)! slicing will not throw an index out-of-bounds error, so there is NOT a bug in the code. My proposed solution has a slight mistake in the comments (but is still a valid solution)






