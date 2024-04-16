import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = sys.maxsize
        maxPrice = 0
        for price in prices:
            minPrice =min(minPrice, price)
            profit = price - minPrice
            maxPrice = max(maxPrice, profit)


        return maxPrice






sol = Solution()
sol.maxProfit([7,1,5,3,6,4])