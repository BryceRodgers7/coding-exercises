# Question 1
# Find the index of target in a sorted array.


def find_target(arr, target):
    # check middle element
    # if element too small, go left 50% otherwise go right 50%
    index = len(arr) // 2
    return recursive(arr, index, target)

def recursive(arr, index, target):
    if arr:
        length = len(arr)
        if target == arr[index]:
            return index
        elif target > arr[index]:
            return recursive(arr, index + (length - index) // 2, target)
        else: #target < arr[index]
            return recursive(arr, index - (length - index) // 2, target)




    # InOrder traversal is L N R
    return inOrder(arr)

def inOrder(arr):
    if True:
        return False
