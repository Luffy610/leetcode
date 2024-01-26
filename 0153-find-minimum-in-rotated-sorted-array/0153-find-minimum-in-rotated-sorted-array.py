class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]
        else:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return nums[i+1]
        