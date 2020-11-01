from typing import  List

class Solution:
    def two_sum(arr,target):
        seen,result={},[]
        for i in arr:
            if target-i in seen:
                if [i,target-i] not in result: result.append([i,target-i])
            seen[i]=True
        return result
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result,seen=[],{}
        for i in range(len(nums)):
            if nums[i] in seen:
                #answer set for this number has been found before
                continue
            prospective_set=[nums[i]]
            target=0-nums[i]
            for j in Solution.two_sum(nums[i+1:],target):
                j=sorted(prospective_set+j)
                result.append(j)
            seen[nums[i]]=True
        return result
    
print (Solution().threeSum([-1,0,1,2,-1,-4]))