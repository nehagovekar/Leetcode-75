'''
Encode and Decode Strings
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        #initialize the result encoded string
        enc_str = ""
        for s in strs:
            #append string with +
            #convert the integer to string
            enc_str += str(len(s)) +"#"+s
        print(enc_str)
        return enc_str

      
    def decode(self, s: str) -> List[str]:
        #initialize result list
        res=[]
        i=0
        p = ""
        #4#neet4#code4#love3#you

        #while loop to traverse the encoded string 
        while i< len(s):
            j=i
            #So, i gives a word/string and we want to find the
            #length which is before '#'
            while s[j]!='#':
                j +=1
               
            length=int(s[i:j])
            #we want to slice the word first
            p= s[j+1:j+1+length]
            res.append(p)
            i= j+length +1
        return res
            
        





