class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        else:
            s_map = {}
            t_map = {}
            for i in s:
                s_map[i] = s_map.get(i,0) + 1
            for j in t:
                t_map[j] = t_map.get(j,0) + 1
            for key,value in s_map.items():
                if value != t_map.get(key):
                    return False
            else:
                return True
        