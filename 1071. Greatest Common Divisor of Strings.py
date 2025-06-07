'''
1071. Greatest Common Divisor of Strings
Solved
Easy
Topics
premium lock icon
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 != str2+ str1):
            return ""
        
        def gcd_length(a,b):
            while b!=0:
                a,b = b, a%b
            return a
    
        #a function for GCD LENGTH PASSING THE LENGTH
        gcd_len = gcd_length(len(str1),len(str2))
            
        #GCD is the common non duplicate letters
        return str1[:gcd_len]