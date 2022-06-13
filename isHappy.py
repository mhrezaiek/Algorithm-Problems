class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        
        while True:
            l = [int(x)for x in str(n)]
            if l in visited:
                return False
            visited.append(l)
            s = 0 
            for num in l:
                s += int(num)**2
            if s == 1:
                return True
            elif s<1:
                return False 
            n = s
                
