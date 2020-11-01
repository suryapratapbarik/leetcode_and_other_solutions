class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        else:
            for _ in range(1,32):
                if n == (2**_): return True
            return False
    
print (Solution().isPowerOfTwo(6))