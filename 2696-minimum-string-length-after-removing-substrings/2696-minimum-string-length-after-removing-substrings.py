class Solution:
    def minLength(self, s: str) -> int:
        while True:
            if "AB" in s:
                s = s.replace("AB","")
                continue
            elif "CD" in s:
                s = s.replace("CD","")
            else:
                break
        return len(s)

        