class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0 
        for i , n in enumerate(digits):
            num+=digits[len(digits)-1-i]*10**i
        num += 1 
        return [int(x) for x in str(num)]
        
