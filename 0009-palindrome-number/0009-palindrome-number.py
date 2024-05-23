class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        if x < 0:
            return False
        else:
            temp = x
            while x > 0:
                reminder = x % 10
                reverse = (reverse) * 10 + reminder
                x = x // 10
            print(reverse)
            if temp == reverse:
                return True
            else:
                return False
        