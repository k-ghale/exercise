
import math

def maxProfit(self, prices):
    profit = 0
    buy = prices[0]
    n = len(prices)

    for i in range(1, n):
        if prices[i]< buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy

    return profit

