class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max = 0
        for i in strs:
            if i.isnumeric():
                if max < int(i):
                    max = int(i)
            elif i.isalnum():
                if max < len(i):
                    max = len(i)
        return max
        
        