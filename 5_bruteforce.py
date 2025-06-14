'''
345. Reverse Vowels of a String
Solved
Easy
Topics
premium lock icon
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=("aeiouAEIOU")
        s=list(s)

        collected = [v for v in s if v in vowels]
        reversed_vowels= collected[::-1]
     #   return reversed_vowels

        j=0
        for i in range (0,len(s)):
            if s[i] in vowels:
                s[i]=reversed_vowels[j]
                j+=1

        return ''.join(s)
   
        

        