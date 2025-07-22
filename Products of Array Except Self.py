'''
Products of Array Except Self
Solved 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #since we want the product of all the numbers before that number to be saved on that index
        prefix=1
        # we know res length is fixed
        res=[1] * len(nums)
        #iterate through num to save the product before that index position to that position

        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]
        postfix=1

        for i in range(len(nums)-1, -1, -1):
            #remember to multiply it to prev prefix values in res
            res[i] *= postfix
            postfix*=nums[i]

        return res

        '''
        mistake 1: Getting confused between whether i, n if you want that use enumerate when range its for indices
        mistake 2: *= should not have space
        mistake 3: dont forget when you want two things prefix and postfix traversal its better to make another list for rest
        mistake 4: result can have the len(nums) if length is fixed save space
        remember: list-->res[i] understand what you are trying to append its list here

        '''