#leetcode Sliding Window: Best Time to Buy and Sell Stock - Leetcode 121 - Python
test = [1,5,2,5,1,2]
def maxProfit(prices):
    l, r = 0, 1 #left=buy right=sell
    maxP = 0

    while r < len(prices):
        #profitable
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP
print(maxProfit(test))

        
        
 











