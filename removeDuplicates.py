class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        head = 1
        for head in range(1,len(nums)):
            if nums[i]!=nums[head]:
                nums[i+1] = nums[head]
                i = i +1
        return i +1 

