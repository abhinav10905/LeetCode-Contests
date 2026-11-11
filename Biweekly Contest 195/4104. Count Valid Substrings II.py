**QUESTION**
4104. Count Valid Substrings II
You are given a string s consisting only of the characters 'a', 'b', and 'c'.
A string is called valid if it does not contain "abc" as a subsequence.
Return the number of valid substrings in s. Substrings with different starting or ending indices are counted separately.

 **CONSTRAINTS**
1 <= s.length <= 105​​​​​​​
s only consists of 'a', 'b', and 'c' characters.

**CODE**
class Solution:
    def countValidSubstrings(self, s: str) -> int:
        a=-1
        ab=-1
        abc=-1
        c=0
        for i in range (0,len(s)):
            if s[i]=="a":
                a=i
            elif s[i]=="b":
                ab=a
            else:
                abc=ab
            c+=(i-abc)
        return c
        
