class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        if nums[left] > target:
            return left
        else:
            return left+1
        # elif nums[middle] < target:
        #     return middle + 1
        