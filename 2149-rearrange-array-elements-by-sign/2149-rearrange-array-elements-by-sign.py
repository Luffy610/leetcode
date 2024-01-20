class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        ans = []
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans 