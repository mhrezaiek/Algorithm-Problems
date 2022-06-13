class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum())
        s = s.lower()
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True
