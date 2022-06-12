class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range(len(str(x))//2):
            num = list(str(x))
            if num[i]!= num[len(num)-1-i]:
                return False
        return True
                
