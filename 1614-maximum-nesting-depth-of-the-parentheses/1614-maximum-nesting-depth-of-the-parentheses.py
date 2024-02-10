class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        stack = []
        count = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ")":
                if maximum < len(stack):
                    maximum = len(stack)
                stack.pop()
        return maximum
                

        