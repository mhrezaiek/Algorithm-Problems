class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i , num in enumerate(nums):
            if num not in dic:
                dic[num] = i
            elif abs(dic.get(num) - i)<= k:
                return True
            else: 
                dic[num] = i
        return False
