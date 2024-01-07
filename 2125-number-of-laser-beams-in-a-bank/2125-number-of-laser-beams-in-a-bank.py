class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = []
        mul = []
        res = 0
        for i in range(len(bank)):
            l = []
            temp = list(bank[i])
            for j in range(len(temp)):
                if temp[j] == '1':
                    l.append([i,j])
                else:
                    continue
            if len(l) > 0:
                ans.append(len(l))
        for i in range(len(ans)-1):
            mul.append(ans[i]* ans[i+1])
        return sum(mul)
    