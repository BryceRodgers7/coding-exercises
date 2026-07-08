# Question 1
# Find the maximum sum of a subarray of size k.
# nums = [2,1,5,1,3,2]
# k=3












































def max_sum(nums: list[int], k: int):
    # scan thru keeping a running total, add next/subtract last & compare to running max

    if not nums or len(nums) < k or k <= 0:
        return -1
    
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        if curr_sum > max_sum:
            max_sum = curr_sum
        
    return max_sum

def max_subarray_k(arr, k):

    # scan thru with sliding window, adding next & subtracting last, checking for max

    if not arr or len(arr) < k or k <= 0:
        return None
    
    hi = cur_sum = sum(arr[:k])
    
    for i in range(len(arr) - k):
        cur_sum += arr[k + i]
        cur_sum -= arr[i]
        if cur_sum > hi:
            hi = cur_sum

    return hi


def max_subarray(arr, k):

    # scan thru adding next number & subtracting last number, checking for new high


    if not arr or len(arr) < k or k <= 0:
        return None

    current_sum = sum(arr[:k])
    high = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i]
        current_sum -= arr[i - k]
        if current_sum > high:
            high = current_sum
        
    return high


def sum_subarr(arr, k):
    # sum first k, then scan thru adding next element & subtracting previous element

    if not arr or len(arr) < k or k <= 0:
        return None
    
    cur_sum = sum(arr[:k])
    result = cur_sum

    for i in range(len(arr) - k):
        cur_sum -= arr[i]
        cur_sum += arr[i + k]

        if cur_sum > result:
            result = cur_sum
    
    return result

def max_sum_subarray(arr, k):
    # scan thru arr, adding next element and subtracting last, checking for max
    if not arr or len(arr) < k or k <= 0:
        return None
    
    cur_sum = sum(arr[:k])
    result = cur_sum

    for i in range(len(arr) - k):
        cur_sum += arr[k + i]
        cur_sum -= arr[i]
        if cur_sum > result:
            result = cur_sum

    return result

def max_sum(nums, k):
    # scan thru adding only next num and subtracting last num, checking for max
    if not nums or len(nums) < k or k <= 0:
        return None
    
    cur_sum = sum(nums[:k])
    result = cur_sum

    for i in range(len(nums) - k):
        cur_sum += nums[i + k]
        cur_sum -= nums[i]

        if cur_sum > result:
            result = cur_sum

    return result

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




def longest_substr(s: str) -> int:
    # scan thru, use set to keep track of seen chars, shrink set from left if current char is already in set

    if not s:
        return -1
    
    seen = set()
    left = right = longest = 0


    for ch in s:
        while ch in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(ch)
        right += 1

        if len(seen) > longest:
            longest = len(seen)

    return longest

def longest_nonrep_substr(s):

    # scan thru with 2 pointers, maintain set of seen chars, shrink when next is seen & grow when next is unseen

    if not s:
        return -1
    
    left = 0
    seen = set()
    result = 0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[i])
        if len(seen) > result:
            result = len(seen)

    return result


def longest_substr(s):
    # put seen chars in a set, scan thru until next char is seen, then shorten substr until its not-seen
    if not s or len(s) == 0:
        return None
    
    seen = set()
    left = 0
    result = 0

    for i in range(len(s)):

        while s[i] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[i])

        if len(seen) > result:
            result = len(seen)

    return result

def longest_substr(s):
    # scan thru, keeping track of 'seen' chars, if next char is seen, shrink window from left until it is not seen
    if not s or len(s) == 0:
        return None
    
    seen = set()
    left = 0
    result = 0

    for i in range(len(s)):

        while s[i] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[i])

        if len(seen) > result:
            result = len(seen)

    return result

def longest_substr(s):
    # scan thru keeping track of 'seen' with a set
    # if the next char is 'seen', remove from the left until not-seen, check for max length / set size
    result = 0
    if not s or len(s) < 1:
        return result
    
    seen = set()
    left = 0

    for i in range(len(s)):

        while s[i] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[i])

        if len(seen) > result:
            result = len(seen)
    
    return result

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