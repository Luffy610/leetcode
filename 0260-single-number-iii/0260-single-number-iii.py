class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        countNums={}
        for i in range(len(nums)):
            countNums[nums[i]] = countNums.get(nums[i], 0) + 1
        for num, value in countNums.items():
            if value == 1:
                ans.append(num)
        return ans