class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = -1
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        while (left <= right):
            middle = (left + right) // 2
            if nums[middle] == target:
                ans = middle
                break
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1  
        if ans == -1:
            return [-1, -1]
        else:   
            i = ans
            j = ans 
            print(i,j,ans)
            while(i >= 0 and nums[i] == target):
                i = i - 1
            while(j < len(nums) and nums[j] == target):
                j = j + 1
            return [i+1,j-1]