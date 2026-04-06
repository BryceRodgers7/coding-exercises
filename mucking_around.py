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








# Write a Python function group_anagrams(strs) that groups anagrams together. Return a list of lists.

# example: words = ['bat', 'tab', 'blah', 'holla', 'holal', 'alloh'] should return a list with 3 lists (last 3 words, first 2 words, and 3rd word alone)

def group_anagrams(strs):
    groups = {}

    for word in strs:
        key = sorted(word)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())

# this seems correct, should I lower-case everything & remove whitespace? 
# complexity: this runs in O(n) time and uses O(n) extra space

# WRONG, no lower-case. sorted(word) returns a list which is not hashable, need to wrap that in tuple() to make it a hashable key. Also the run-time is O(N * k log k) because k elements need to be sorted , each taking log(k) time.


 








 # Write a Python function top_k_frequent(nums, k) that returns the k most frequent elements in the list.


def top_k_frequent(nums, k):
    freq = {}

    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    sorted_items = sorted(freq.items(), key=lambda x: x[1])

    result = []
    for i in range(k):
        result.append(sorted_items[i][0])

    return result





# the solution is incorrect because sorted() sorts it in ascending order, so taking the first k elements will yield the least frequent, not the most frequent.
# to fix this, give the reverse=true argument to sorted()
# complexity: O(n + n log n + k) time with O(n) extra space 





# Write a function that removes duplicates from a list while preserving order.

def remove_duplicates(nums):
    seen = set()
    result = []

    for n in nums:
        if n not in seen:
            result.append(n)
            seen.add(n)

    return result

# this is correct but uses extra space because it creates a new list instead of removing duplicates from the original list.
# to fix this, change the loop so it removes elements already seen, and adds them to seen otherwise, then return the original list.
# complexity: O(n) time with O(n) extra space but an improved version runs in O(n) times with O(1) extra space

# fixed
def remove_duplicates(nums):
    seen = set()

    for n in enumerate(nums):
        if n in seen:
            nums.remove(n)
        else:
            seen.add(n)

    return nums





# Write a function that returns a list of squares from 0 to n.

def squares(n, result=[]):
    for i in range(n + 1):
        result.append(i * i)
    return result

# this is partially correct, it will keep appending to the existing 'result' each time it is called. Also  it could be more concise with list comprehension
# to fix this, the parameter result should default to None, and be initialized as an empty list inside the function (if it is none)
# complexity: O(n) time with O(n) extra space, unchanged for the improved solution

# fixed
def squares(n, result=None):
    if result is None:
        result = []
    for i in range(n + 1):
        result.append(i * i)
    return result






# Return True if a list contains duplicates. (choose best answer)

# A
def has_duplicates(nums):
    return len(nums) != len(set(nums))

# B
def has_duplicates(nums):
    seen = []
    for n in nums:
        if n in seen:
            return True
        seen.append(n)
    return False

# Answer A is better but both are technically correct. Answer B is less efficient because its runtime is O(n * n)
# Complexity: A is O(n) time with O(n) extra space, while B is O(n * n) time with O(n) extra space







# Find the maximum number in a list.

def find_max(nums):
    max_val = 0
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val


# this is incorrect because it will return 0 if all the numbers are negative.
# To fix, it should check for an empty list, otherwise use the first real value in the list as the running max_val
# complexity: O(n) time with O(1) extra space (same for fixed code)

# fixed
def find_max(nums):
    if len(nums) < 1:
        return None
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val








# Count occurrances of each character in a string


def count_chars(s):
    counts = {}
    for ch in s:
        counts[ch] += 1
    return counts

# This code is incorrect because it will throw a KeyError for each character in the dict.
# instead of count[ch] += 1 it should use counts[ch] = counts.get(ch, 0) + 1
# complexity is O(n) time with O(n) extra space (same for fixed code)

def count_chars(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts






# Reverse a list

# A
def reverse_list(lst):
    return lst[::-1]

# B
def reverse_list(lst):
    result = []
    for i in range(len(lst)):
        result.insert(0, lst[i])
    return result


# Answer A is better because it is more pythonic, it uses a list-slicing step to keep the code concise. Answer B is correct but less concise.
# Complexity is same for both A and B: O(n) time and O(n) extra space 




# Return the last element of a list

def last_element(nums):
    return nums[len(nums)]


# this is incorrect it will throw an IndexException
# to fix this, use len(nums) - 1 or just index the -1 position
# complexity: O(1) time (same for fixed code)

def last_element(nums):
    return nums[-1]



# Merge two dictionaries, summing values for shared keys

def merge_dicts(a, b):
    result = a

    for key in b:
        if key in result:
            result[key] += b[key]
        else:
            result[key] = b[key]

    return result


# This is correct but could be more 'pythonic' and concise.
# to improve this, use result[key] = result.get(key, 0) + b[key]  instead of the if-else
# complexity: O(n) time where n is the length of b, and O(m + n) extra space where m is the length of a.

# fixed
def merge_dicts(a, b):
    result = a

    for key in b:
        result[key] = result.get(key, 0) + b[key]

    return result





# Sort a list of strings by length

def sort_by_length(words):
    return sorted(words, key=len())

# this is incorrect because the key parameter will throw an error.
# to fix this use key=lambda x: len(x) that will make sort correctly use the length of each word/string
# complexity: O(n log n) time with O(n) extra space

# fixed
def sort_by_length(words):
    return sorted(words, key=lambda x: len(x))





# Return True if list is not empty

def is_not_empty(nums):
    if nums == []:
        return False
    else:
        return True
    

# this is not correct, the comparison will throw an error.
# to fix this, use if len(nums) == 0: return False 
# complexity: O(1) time with no extra space (same for fixed code)


def is_not_empty(nums):
    if len(nums) == 0:
        return False
    else:
        return True
    

    