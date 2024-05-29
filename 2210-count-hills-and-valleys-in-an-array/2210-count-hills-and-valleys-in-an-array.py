class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums)-1):
            # edge case, the same velly!
            # adjacent indexes should be considered as one velly or hill
            # to handle this, we can check if next value is the same as current
            # for example in [4,1,1,6]
            # [4, 1(we are here), 1(detected next value), 6]
            # replace the first 1 by 4 (4 is a previous value)
            # as result we get: [4,4,1,6]
            # so thet at the next iteration the second 1 will be detected as a valley
            # [4,4,1(we are here),6] 
            # 4 > 1 < 6
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            elif nums[i-1] > nums[i] < nums[i+1] or nums[i-1] < nums[i] > nums[i+1]:
                result += 1
        return result
            

            


            