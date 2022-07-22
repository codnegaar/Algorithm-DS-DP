'''
Leetcode_350_Intersection of Two Arrays II
 
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2,2]
        
Example 2:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [4,9]
        
Explanation: [9,4] is also accepted.

'''
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        result = []
        cnt =Counter(nums1)
        
        for num in nums2:
            if cnt[num]> 0:
                result.append(num)
                cnt[num]  -=1
        return result
                
