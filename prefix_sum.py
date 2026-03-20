# Question 1
# Count the number of subarrays that sum to k.
# Example:
# nums=[1,1,1,3,4,5,8,2,4,5,1]
# k=2











































def num_subarrays(arr, k):
    # calculate prefix sums hash, checking for any current_sum - k in prefix sums (if so add count for that prefix_sum to running total)
    if not arr:
        return 0

    prefix_sums = {0 : 1}
    cur_sum = 0
    count = 0

    for i in range(len(arr)):
        cur_sum += arr[i]

        if cur_sum - k in prefix_sums:
            count += prefix_sums[cur_sum - k]

        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

    return count


def num_sum_subarrays(nums, k):
    # create prefix_sum hash, along the way scan for any case where (current_sum - k) is in prefix_sums
    
    prefix_sums = {0 : 1}
    cur_sum = 0
    result = 0

    for i in nums:
        cur_sum += i

        if cur_sum - k in prefix_sums:
            result += prefix_sums[cur_sum - k]

        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

    return result

def count_subarrays(arr, k):
    # calculate prefix sums, scan thru looking for current_sum - k equal to any previous prefix

    prefix_sums = {0 : 1}
    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num

        if current_sum - k in (prefix_sums):
            count += prefix_sums[current_sum - k]

        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count


def sum_to_k(nums, k):
    # calculate prefix sums in a hashmap
    # scan thru looking for prefix - k = some previous prefix

    prefix_sums = {0: 1}
    current_sum = 0
    result = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        
        if (current_sum - k in prefix_sums):
            result += prefix_sums[current_sum - k]

        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return result


def sum_subarr(nums, k):
    # scan thru and track current running sum, and how many times we've seen that sum before in a hashmap (prefix_sum_counts)
    # if we see that current running sum (aka prefix_sum) - k matches another prefix, then the subarray between i & current (j) is valid
    sum = 0
    prefix_sum_counts = {0 : 1}
    count = 0
    
    for num in nums:
        sum += num

        if sum - k in prefix_sum_counts:
            count += prefix_sum_counts[sum - k]

        prefix_sum_counts[sum] = prefix_sum_counts.get(sum, 0) + 1

    return count









# Question 2
# Create a class that supports fast range sum queries.
# sumRange(i,j) inclusive
# array sample = [5, 6, 7, 8, 9, 11, -1, 22, 0, 24]













































class fastSummer():
    # calculate prefix_sums then subtract prefix_sums[i] from prefix_sums[j]

    def __init__(self, arr):
        if not arr:
            return None
        
        self.prefix_sums = [0]
        cur_sum = 0

        for i in range(len(arr)):
            cur_sum += arr[i]
            self.prefix_sums.append(cur_sum)

    def sumRange(self, i, j):
        if i < 0 or j > (len(self.prefix_sums) - 2) or i > j:
            return None
        
        return self.prefix_sums[j + 1] - self.prefix_sums[i]


# create prefix_sums array and subtract element i from element j
class myClass():

    def __init__(self, arr):
        self.prefix_sums = [0]
        cur_sum = 0

        for num in arr:
            cur_sum += num
            self.prefix_sums.append(cur_sum)

    def sumRange(self, i, j):
        if i > j or i < 0 or j >= len(self.prefix_sums) - 1:
            return None
        return self.prefix_sums[j + 1] - self.prefix_sums[i]

# create class that takes an array as constructor
class fast_range_sums:
    # initialize prefix_sums on creation
    

    def __init__(self, arr):
        self.prefix_sums = [0]
        running_sum = 0

        for i in range(len(arr)):
            running_sum += arr[i]
            self.prefix_sums.append(running_sum)

    # sumRange will subtract prefix[j] from prefix[i] and return
    def sumRange(self, i, j):
        if i < 0 or j >= len(self.prefix_sums) - 1 or i > j:
            return None
        
        return self.prefix_sums[j + 1] - self.prefix_sums[i]
    



class fastSumRange:

    def __init__(self, arr):
        self.prefixes = []
        running_sum = 0

        for num in arr:
            running_sum += num
            self.prefixes.append(running_sum)


    def sumRange(self, i, j):
        if i == 0:
            return self.prefixes[j]
        sum = self.prefixes[j] - self.prefixes[i - 1]

        return sum
