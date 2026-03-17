# Question 1

# Generate all subsets of [1,2,3].
































def all_subsets(arr):
    # convert to array
    # scan thru array with recursive function
    # append current element then call for all remaining elements

    result = []

    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(arr)):
            backtrack(i + 1,path + arr[i])

    backtrack(0, [])
    return result



# Question 2

# Generate all permutations of [1,2,3].




































def all_permutations(arr):
    result = []

    def backtrack(remaining, current):
        if not remaining:
            result.append(current)
            return
        
        for i in range(len(remaining)):
            backtrack(remaining[:i] + remaining[:i+1], current + remaining[i])

    backtrack(arr, [])
    return result