class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1 = list(s)
        visited = []
        for i in range(len(s1)):
            if s1[i] not in visited and s1.count(s1[i]) == 1:
                return i 
            else:
                visited.append(s[i])
                continue
        return -1 

        