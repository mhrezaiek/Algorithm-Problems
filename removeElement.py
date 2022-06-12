class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        for head in range(0, len(nums)):
            if nums[head] != val:
                nums[i] = nums[head]
                i +=1 
        return i  
        
