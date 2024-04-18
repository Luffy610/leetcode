class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            index = nums2.index(i)
            if index == len(nums2)-1:
                res.append(-1)
                continue
            temp = max(nums2[index+1::-1])
            if temp > nums2[index]:
                res.append(temp)
            else:
                res.append(-1)
        return res    
        