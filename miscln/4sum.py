
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            ls = sorted([nums[i], nums[j], nums[k], nums[l]])
                            tuple_key = tuple(ls)
                            if tuple_key not in output:
                                output[tuple_key] = 1
        
        return [list(key) for key in output]
    
print (Solution().fourSum([-5,5,4,-3,0,0,4,-2],
4))