class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        stack = 0
        count = 0
        for i in s:
            if i == '(':
                stack += 1
            elif i == ")":
                if maximum < stack:
                    maximum = stack
                stack -= 1
        return maximum
                

        