class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            dic[numbers[i]] = i
        for i, n  in enumerate(numbers):
            if target-n in dic and dic[target-n]!= i:
                return [i+1 , dic[target-n]+1]
