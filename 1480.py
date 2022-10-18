# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

# loop through array and add new number with the result of the last addition
# keep those results individually and in order in a list

def main():
    nums = [1, 2, 3, 4]
    sums = []
    last = 0
    for n in nums:
        last += n
        sums.append(last)
    
    print(sums)

# gotta find a fix for the index problem in a python for loop
# def better_solution():
#     nums = [1, 2, 3, 4]
#     for n in range(len(nums)):
#         nums[n] += nums[n - 1]
    
#     return nums

main()
# print(better_solution())
