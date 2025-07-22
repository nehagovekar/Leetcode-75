'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        #initialize with defaultdict so that you dont have to worry about missing vals
        result = defaultdict(list)

        for s in strs:
            #now we have the strings in the list one by one
            #what we will do first if create a list of 26 characters for counting
            #should be initialized to 0 for counting
            count=[0] * 26

            for i in s:
                #we have letters but dont forget to mention ASCII characters while counting
                count[ord(i)-ord('a')] +=1
            result[tuple(count)].append(s)

        return list(result.values())
            
              


        '''
        mistake 1: count[ord(i)-ord('a')]+=1
        mistake 2: when it is giving an output but just aprtially your return statement is in the wrong tab
        mistake 3: understand the logic of count for ascii it will help you
        mistake 4: tuple is tricky for group anagrams
        mistake 5: list not List, defaultdict not anything else

        '''
        