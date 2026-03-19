# Question 1

# Generate all subsets of an array
# arr = [1,2,3].










































def gen_subsets(arr):
    # starting with empty set, add the current_subset 
    # then for each element, recursively call/add the next element to that current subset
    result = []

    def backtrack(next_index, curr_subset):
        result.append(curr_subset)

        for i in range(next_index, len(arr)):
            backtrack(i + 1, curr_subset + [arr[i]])

    backtrack(0, [])

    return result
    
    

def all_subsets(arr):
    # convert to array
    # scan thru array with recursive function
    # append current element then call for all remaining elements

    result = []

    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(arr)):
            backtrack(i + 1,path + [arr[i]])

    backtrack(0, [])
    return result



# Question 2

# Generate all permutations of [1,2,3].































def all_permutations(arr):
    result = []

    def backtrack(remaining_elements, current_permutation):
        if not remaining_elements:
            result.append(current_permutation)
            return
        
        for i in range(len(remaining_elements)):
            backtrack(
                remaining_elements[:i] + remaining_elements[i+1:],
                current_permutation + [remaining_elements[i]]
            )

    backtrack(arr, [])
    return result