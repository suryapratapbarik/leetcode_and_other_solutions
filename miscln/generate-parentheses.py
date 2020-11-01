from typing import List
class Solution:
    res = []
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        self.recurseFn(n, self.res, "(", 1)
        return self.res
        
    def recurseFn(self, n, res, s, val):
        if val is 0 and len(s) is n*2:
            res.append(s)
        elif len(s) < n*2:
            if val < n:
                self.recurseFn(n, res, s + "(", val+1)
            if val > 0:
                self.recurseFn(n,res, s+")", val-1)
                
                
print (Solution().generateParenthesis(1))