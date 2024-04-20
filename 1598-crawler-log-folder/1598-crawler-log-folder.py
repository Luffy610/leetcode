class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == "../":
                if len(stack) == 0:
                    continue
                else:
                    stack.pop(-1)
            elif i == "./":
                continue
            else:
                stack.append(i)
        return len(stack)
