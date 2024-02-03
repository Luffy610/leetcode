class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        empty_list = list()
        anagram_maps = defaultdict(list)
        for i in range(len(strs)):
            temp = ''.join(sorted(list(strs[i])))
            anagram_maps[temp].append(strs[i])
        return(list(anagram_maps.values()))



        
        