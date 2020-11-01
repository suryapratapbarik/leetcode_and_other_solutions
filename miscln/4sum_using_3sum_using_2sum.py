from typing import  List

class Solution:
    def twoSum(arr,target):
        seen,result={},[]
        for i in arr:
            if target-i in seen:
                if [i,target-i] not in result: result.append([i, target-i])
            seen[i]=True
        return result
    
    def threeSum(nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        result,seen=[],{}
        for i in range(len(nums)):
            if nums[i] in seen:
                #answer set for this number has been found before
                continue
            prospective_set = [nums[i]]
            sub_target = target - nums[i]
            for j in Solution.twoSum(nums[i+1:], sub_target):
                j=sorted(prospective_set+j)
                result.append(j)
            seen[nums[i]]=True
        return result
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        result,seen=[],{}
        for i in range(len(nums)):
            if nums[i] in seen:
                #answer set for this number has been found before
                continue
            prospective_set = [nums[i]]
            sub_target = target - nums[i]
            for j in Solution.threeSum(nums[i+1:], sub_target):
                j=sorted(prospective_set+j)
                result.append(j)
            seen[nums[i]]=True
        return result
    
print (Solution().fourSum([-5,5,4,-3,0,0,4,-2],4))
#[[-5, 0, 4, 5], [-3, -2, 4, 5]]