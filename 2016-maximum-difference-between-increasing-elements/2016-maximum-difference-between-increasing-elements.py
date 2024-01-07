class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max = 0 
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                elif i < j and max < (nums[j] - nums[i]):
                    print(nums[i], nums[j])
                    max = nums[j] - nums[i]
        if max == 0:
            return -1
        else:
            return max