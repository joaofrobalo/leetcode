# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly 
# to the left of the index is equal to the sum of all the numbers 
# strictly to the index's right.
# If the index is on the left edge of the array, 
# then the left sum is 0 because there are no elements to the left. 
# This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1. 

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

# Constraints:
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

def main():
    print(f"Index of pivot is: {pivotIndex([-1,-1,-1,-1,-1,0])}")
    print(f"Faster: {better([1,7,3,6,5,6])}")

def pivotIndex(nums):
    # gets a list of nums
    # looping n through the list
    # adds all previous numbers of the list and all the following numbers of the list and checks if same
    # if same, then current n is pivot, if not then keep looping
    # if never same then return -1
    s_backwards = 0
    for i, n in enumerate(nums):
        s_forward = sum(nums[i+1:])
        if s_backwards == s_forward:
            return i
        s_backwards +=n
    return -1

def better(nums):
    # better solution from MaksymSkorupskyi
    # instead of calling sum() every iteration just call it once and then subtract
    # the nums from it. Means sumR will gradually update to remove the nums to the left
    # of the potential pivot index
    sumL = 0
    sumR = sum(nums)
    for i in range(len(nums)):
        sumR -= nums[i]
        if sumL == sumR:
            return i
        sumL += nums[i]
    return -1
    

main()