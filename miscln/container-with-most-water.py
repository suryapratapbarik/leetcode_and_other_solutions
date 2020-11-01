class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, maxArea = 0, len(height)-1, 0 
        while l!=r:
            if height[l]<height[r]:
                maxArea = max([maxArea, height[l]*(r-l)])
                l+=1
            else:
                maxArea = max([maxArea, height[r]*(r-l)])
                r-=1
        return maxArea
        