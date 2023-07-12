# 121
# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by:
    -choosing a single day to buy one stock and 
    -choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

"""


p = [7,1,5,3,6,4]
# Using two pointers two iterate over the array
# we look for a profibale ocasion where r ptr is > that left ptr
# if profitable calculate the max pro
# if not l ptr = r ptr because is r ptr is minor so that means possible or better profit
# always we iterate r ptr

def maxProfit(prices: list[int])-> int:
    l = 0
    r = 1
    mxProfit = 0
    while r < len(prices):
        # profitable?
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            mxProfit = max(mxProfit, profit)
        else:
            l = r
        r+=1
    return mxProfit



sol = maxProfit(p)
print(sol)