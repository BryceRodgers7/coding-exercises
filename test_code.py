
def binary_search(nums, target):
# repeatedly check midpoint, eliminate half of the remaining search space depending on > or <. Assume return -1 for empty list, and any matching index if multiple matches are present.
  result = -1
  left = 0
  right = len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    if nums[mid] > target:
      right = mid - 1
    else: # nums[mid] < target or left == right and target is not present
      left = mid + 1
  return result


print(binary_search([1,2,3,4,5,6,7,8], 8))
print(binary_search([], 8))
print(binary_search([1,1,1,4,5,6,7,8], 1))
print(binary_search([1,2,3,4,5,6,7,8,9], 5))
print(binary_search([1,2,3,4,5,6,6,6,7,8], 6))
print(binary_search([1,2,3,4,50,60,60,77,88], 6))

