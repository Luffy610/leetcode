class Solution:
    def binary_search(self,nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right)// 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        else:
            return -1
    def search(self, nums: List[int], target: int) -> int:
        temp = -1
        if nums[-1] >= nums[0]:
            temp = 0
        else:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    temp = i + 1
                    break
        print(temp)
        if nums[temp] == target:
            return temp
        elif nums[temp] < target <= nums[-1]:
            print(True)
            res = self.binary_search(nums[temp+1:len(nums)], target)
            if res == -1:
                return -1
            else:
                return res + temp + 1
        else:
            print("here")
            res = self.binary_search(nums[0:temp],target)
            if res == -1:
                return -1 
            else:
                return res 
                

        