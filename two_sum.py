'''
Two Sum
Solved 
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a map to check if the target-num is already in the list
        prevMap= {}
        #use enumerate when index and number, enumerate does not need len(num) just num
        for i,n in enumerate(nums):
            #get the second number we need
            diff = target - n
            #if difference is in previous map get the indexex
            if diff in prevMap:
                #one index is the diff found right now --> i and next will be the index of pair found in prevMap
                return [prevMap[diff], i]
            #did a mistake here the last time, remember we want the number to have index
            prevMap[n]=i

