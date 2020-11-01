from typing import List
class Solution:
    def isMutipleOf3(n:int) -> bool:
        if n<0: n*=-1
        if n==0: return True
        if n==1: return False
        odd_bit_count, even_bit_count = 0, 0
        while n>0:
            if n&1==1: odd_bit_count+=1
            n = n>>1
            if n&1==1: even_bit_count+=1
            n = n>>1
        return Solution.isMutipleOf3(abs(odd_bit_count-even_bit_count))
    
    def main(self, arr: List[int]) -> List[bool]:
        return [Solution.isMutipleOf3(num) for num in arr]
            
            
print (Solution().main([0,1,3,11,15,16,17,21]))