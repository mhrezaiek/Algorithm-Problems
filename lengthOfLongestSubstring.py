class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = maxi = 0 
        
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                maxi = max(maxi , i-start)
                start = dic[s[i]] +1
            dic[s[i]] = i
        return max(maxi , len(s)-start )
