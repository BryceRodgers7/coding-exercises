# Question 1
# Count the number of subarrays that sum to k.
# Example:
# nums=[1,1,1,3,4,5,8,2,4,5,1]
# k=2














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
