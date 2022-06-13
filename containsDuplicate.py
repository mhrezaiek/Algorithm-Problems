class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic.values():
            if i > 1:
                return True 
        return False
