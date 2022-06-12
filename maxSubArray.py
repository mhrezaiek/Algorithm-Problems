class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = maxresult = nums[0]
        for i in range(1, len(nums)):
            currsum = max(currsum+nums[i], nums[i])
            maxresult = max(maxresult, currsum)
        return maxresult
