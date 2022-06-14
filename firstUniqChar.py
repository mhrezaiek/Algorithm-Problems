class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, n in enumerate(s):
            if n not in dic:
                dic[n] =[1,i]
            else:
                dic[n][0] +=1 
        for key , value in dic.items():
            if dic[key][0] ==1:
                return dic[key][1]
            
        return -1
