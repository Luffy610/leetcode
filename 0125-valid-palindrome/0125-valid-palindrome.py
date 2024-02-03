class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        print(temp)
        print(temp[::-1])
        if temp == temp[::-1]:
            return True
        else:
            return False

        