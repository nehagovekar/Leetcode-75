'''
Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=(len(t)):
            return False
        #creating dictionaries for both
        countS, countT = {}, {}
        #gets tricky, since we want to create dictionaries where keys are letters and values are count lets iterate
        for i in range(len(s)):
            #here-->s[i] is the letter of string s --> counts[LETTER]
            countS[s[i]] = 1 + countS.get(s[i],0)          
            countT[t[i]]= 1 + countT.get(t[i],0)

        return countS==countT


       '''
       Input: s = "anagram", t = "nagaram"

i	s[i]	t[i]	countS	                  countT
0	a	    n	{'a': 1}	                       {'n': 1}
1	n	    a	{'a': 1, 'n': 1}	               {'n': 1, 'a': 1}
2	a	    g	{'a': 2, 'n': 1}	               {'n': 1, 'a': 1, 'g': 1}
3	g	    a	{'a': 2, 'n': 1, 'g': 1}	       {'n': 1, 'a': 2, 'g': 1}
4	r   	r	{'a': 2, 'n': 1, 'g': 1, 'r': 1}    	same
5	a   	a	{'a': 3, ...}	{'a': 3, ...}
6	m   	m	{'a': 3, ..., 'm': 1}	same'''

'''
s[i]                # Get the character at position i in string s
countS[s[i]]        # Access the count value of that character in the dictionary
countS.get(s[i], 0) # Try to get the count for s[i]; return 0 if s[i] is not found
1 + countS.get(...) # Add 1 to the current count (or to 0 if the character is new)
countS[s[i]] = ...  # Store the updated count for that character back in the dictionary
'''

        