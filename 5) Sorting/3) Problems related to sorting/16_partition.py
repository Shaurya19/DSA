# Hoare's Partition

def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)-1):
        for j in range(1,len(array)):
            if array[i] + array[j] == targetSum:
                return array[i],array[j]
        
twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)