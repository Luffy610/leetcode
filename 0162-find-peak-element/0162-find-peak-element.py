class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i-1 < 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i + 1 >= len(nums):
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i-1] < nums[i] > nums[i+1]:
                    return i 
