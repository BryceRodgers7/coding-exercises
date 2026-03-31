# Question 1

# Generate all subsets of an array
# arr = [1,2,3].











































def all_subsets(arr):
    # start with empty set, backtrack adding the next element & backtracking for each remaining element

    if not arr:
        return None

    result = []

    def backtrack(next_start_index, cur_subset):
        result.append(cur_subset)

        for i in range(next_start_index, len(arr)):
            backtrack(i + 1, cur_subset + [arr[i]])

    backtrack(0, [])
    return result


def all_subsets(arr):
    # backtrack from empty set
    # recursively add current set to result then call again for all remaining elements

    result = []

    def backtrack(next_start_index, current_subset):
        result.append(current_subset)

        for i in range(next_start_index, len(arr)):
            backtrack(i + 1, current_subset + [arr[i]])

    backtrack(0, [])
    return result


def gen_subsets(arr):
    # starting with empty set, call recursive method 
    # recursive method adds the current set, then for each remaining element, calls with that element + the current subset
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





























def all_perms(arr):
    # write a backtrack funciton and call it with an empty array
    # in backtrack, scan thru the remaining elements, adding the current element & calling again for all remaining elems

    if not arr:
        return None

    result = []

    def backtrack(current_perm, remaining):
        if not remaining or len(remaining) < 1:
            result.append([current_perm])
            return
        
        for i in range(len(remaining)):
            backtrack(current_perm + [remaining[i]],
                      remaining[:i] + remaining[i+1:])
            
    backtrack([], arr)
    return result
            

def all_perms(arr):
    # start with empty set, backtrack; appending the current subset & again backtracking for all remaining elements

    if not arr:
        return None

    result = []

    def backtrack(cur_subset, remaining):
        if not remaining or len(remaining) == 0:
            result.append([cur_subset])
            return
                      
        for i in range(len(remaining)):
            backtrack(cur_subset + [remaining[i]], remaining[:i] + remaining[i + 1:])

    backtrack([], arr)
    return result

def all_perms(arr):
    # backtrack recursively starting with empty set
    # add current set to result then call backtrack for all remaining elements

    result = []

    def backtrack(remaining, current_subset):
        if not remaining or len(remaining) == 0:
            result.append(current_subset)
            return

        for i in range(len(remaining)):
            backtrack(remaining[:i] + remaining[i + 1:],
                      current_subset + [remaining[i]])
            
    backtrack(arr, [])
    return result


def all_perms(arr):
    # call recursive function with all remaining elements & empty current-set
    # recursive function should add current-set and terminate if there are no remaining sets, otherwise call for all remaining sets + the current set
    result = []

    def backtrack(remaining, current_subset):
        if not remaining or len(remaining) == 0: 
            result.append(current_subset)
            return
        
        for i in range(len(remaining)):
            backtrack(remaining[:i] + remaining[i + 1:], 
                      current_subset + [remaining[i]])
            
    backtrack(arr, [])
    return result

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