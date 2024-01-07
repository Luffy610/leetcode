class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            j = i + 1 
            k = i + 2
            while(j < len(nums)-1):
                if(nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]):
                    count += 1
                    k += 1
                elif (nums[i] == nums[k] or nums[j] == nums[k]):
                    k += 1
                elif (nums[j] == nums[i]):
                    j += 1
                    k = j + 1
                if (k > len(nums) - 1):
                    j += 1
                    k = j + 1
        return count
        