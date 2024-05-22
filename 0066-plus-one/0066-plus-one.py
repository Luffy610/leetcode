class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = -1
            while True:
                digits[i] = 0
                i = i-1
                if i < -(len(digits)):
                    digits = [1] + digits
                    break
                elif digits[i] == 9:
                    continue
                else:
                    digits[i] += 1
                    break
        else:
            digits[-1] += 1
        return digits