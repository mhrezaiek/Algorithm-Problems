class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        dic = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"],
               5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],
               8:["t","u","v"],9:["w","x","y","z"]}
        for i  in range(len(digits)):
            if ans:
                ans = self.multi(ans,dic[int(digits[i])] )
            else:
                ans = dic[int(digits[i])]
        return ans
        
        

    def multi(self, l1 , l2):
        ans = []
        for i in range(len(l1)):
            for j in range(len(l2)):
                ans.append((l1[i]+l2[j]))
        return ans
