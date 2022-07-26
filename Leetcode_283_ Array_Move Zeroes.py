'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.


'''

"""
Do not return anything, modify nums in-place instead.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lptr = 0
        for rptr in range (len(nums)):
            if nums[rptr]:
                nums[lptr], nums [rptr] = nums [rptr],  nums[lptr]
                lptr += 1
