class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            s1 = self.poli(s,i,i)
            if len(s1)> len(longest):
                longest = s1
            s2 = self.poli(s, i, i+1)
            if len(s2)>len(longest):
                longest = s2
        return longest
    def poli(self, s,i,j):
        while i >= 0 and j< len(s) and s[i]==s[j]:
            i -= 1
            j += 1 
        return s[i+1: j]
