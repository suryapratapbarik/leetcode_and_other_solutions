import math
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        l, h = 0, len1
        while l<=h:
            xa = (l+h)//2
            xb = ((len1+len2+1)//2) - xa
            a1 = nums1[xa-1] if xa-1>=0 else -math.inf
            a2 = nums1[xa] if xa<len1 else math.inf
            b1 = nums2[xb-1] if xb-1>=0 else -math.inf
            b2 = nums2[xb] if xb<len2 else math.inf
            if a1 <= b2 and b1 <= a2:
                if (len1+len2) % 2 ==0:
                    return sum([max([a1, b1]), min([a2,b2])])/2
                else:
                    return max([a1,b1])
            elif a1 > b2:
                h=xa
            else:
                l=xa+1
                


print(Solution().findMedianSortedArrays([1,3,5,  8,9],                                      [2,4, 6,7,10,12]))
print(Solution().findMedianSortedArrays([1,3],[2]))
print(Solution().findMedianSortedArrays([1,2],[3,4]))
print(Solution().findMedianSortedArrays([0,0],[0,0]))