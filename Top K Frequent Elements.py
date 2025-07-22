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

class Solution(object):
    def topKFrequent(self, nums, k):
        #1.create a hashmap for count
        count= {}
        #create a list of lists to have index (imaginary) and values (list of numbers that have the same count)
      #  freq = [[] for i in range(0, len(nums))]
        freq= [[] for i in range(len(nums)+1)]


        #count the frequency of numbers by iterating the nums now
        for n in nums:
            count[n]=1 + count.get(n,0)
        
        #here, we will have the dicionary with key values which we will traverse to add that to the list freq
        for n,c in count.items():
            freq[c].append(n)
     

        #now we need a result list which has the top k elements
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


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
'''
        mistake 1: freq[c].append(n) -->dont try to append -->freq.append you are appending in that index thats the point
        mistake 2: after one loop to iterate ulta dont forget each i has list so inner foor loop is necessary
        mistake 3: when creating a list of list dont think of it like a dict
        '''


        

        




        