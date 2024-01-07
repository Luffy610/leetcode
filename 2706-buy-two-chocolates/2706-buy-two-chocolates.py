class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        buy = prices[0] + prices[1]
        leftover = money - buy
        if leftover < 0:
            return money
        else:
            return leftover
        