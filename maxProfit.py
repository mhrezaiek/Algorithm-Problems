class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        summ = 0
        for i in range(1,len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            else:
                currsum = prices[i]-mini
                summ = max(summ, currsum)
        
        if summ >0 :
            return summ
        else:
            return 0
                
