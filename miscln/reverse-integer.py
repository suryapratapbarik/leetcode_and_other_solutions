class Solution:
    def reverse(self, x: int) -> int:
        negate = False
        if x<0:
            negate = True
            x = -x
        res = 0;
        while x>0:
            res = res*10 + x%10
            x = x//10
        if negate:
            return -res
        else: return res
        
        
print (Solution().reverse(-321))