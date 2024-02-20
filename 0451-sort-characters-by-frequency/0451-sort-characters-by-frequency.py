import numpy as np
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        count = {}
        for i in set(s):
            count[i] = s.count(i)
        keys = list(count.keys())
        values = list(count.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        for i,j in sorted_dict.items():
            ans += (i*j)
        return ans[::-1]

            
        