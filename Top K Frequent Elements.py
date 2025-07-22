'''
Top K Frequent Elements
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary for counting frequency
        count = {}
        #create an array for the count-value(list of nums) which is freq
        freq= [[] for i in range(len(nums)+1)]
        #simple count how many times each number has occured

        for i in nums:
            count[i] =1 + count.get(i,0)

        for num,cnt in count.items():
            freq[cnt].append(num)
        #Okay, i got confused with res
        #1. remember traversing through range is through indices
        #so once, inside (you want to go through the list in each index hence the second loop)
        #now after appending when it equals to res list then return

        res=[]
        for i in range(len(freq)-1 ,0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res

            
       


        

        




        