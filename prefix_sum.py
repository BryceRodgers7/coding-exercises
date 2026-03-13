# Question 1
# Count the number of subarrays that sum to k.
# Example:
# nums=[1,1,1]
# k=2


# not finished yet I think
def sum_subarr(nums, k):
    # grow subarray right until it matches k or is too large
    # if too large then shrink from left
    res = 0
    if len(nums) < 1:
        return
    left = 0
    sum = nums[0]
    for right in range(len(nums)):
        while sum < k:
            sum += nums[right]
            sum -= nums[left]
