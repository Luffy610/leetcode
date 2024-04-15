class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            temp = prices[i]
            for j in range(i+1,len(prices)):
                if temp >= prices[j]:
                    result.append(temp-prices[j])
                    break
                else:
                    continue
            else:
                result.append(temp)
        return result
                
        