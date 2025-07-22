'''
128. Longest Consecutive Sequence
Solved
Medium
Topics
premium lock icon
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
'''

class Solution(object):
    def longestConsecutive(self, nums):

        #create a set 
        numSet= set(nums)
        #initialize  integer to store max length
        longest = 0
        

        for n in numSet:
            length = 0
            #now we have the numbers and we need to find if we have the start of the sequence
            if (n-1) not in numSet:
                length = 1
                #now we know this is the start of sequence, lets see if we have next number or consecutive numbers
                while (n+1 in numSet):
                    n+=1
                    length+=1
                #out of the while loop we will have max length only if we get out again
            #here
            longest = max(longest, length)

        return longest
      
#mistake 1: understand for loop for the set not the nums
#mistake 2: when the while loop is present remember you are adding the length
#mistake 3: longest was in wrong tab understanf when we use it
