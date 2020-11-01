from typing import List
from collections import Counter

"""class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_dict ={}
        count=0
        for i in A:
            for j in B:
                s = i+j
                if s in sum_dict:
                    sum_dict[s] += 1
                else:
                    sum_dict[s] = 1
        
        for i in C:
            for j in D:
                target = 0 - (i+j)
                if target in sum_dict:
                    count +=target
        return count  """     
# O(n**2) time, O(n**2) space

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = Counter(a+b for a in A for b in B)
        count = sum(AB[-c-d] for c in C for d in D)
        return count


print (Solution().fourSumCount([1,2],
[-2,-1],
[-1,2],
[0,2]))