class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Solution 1: time O(n^2), space O(1)
        # brute force: nested for loop to check every possible pair and find min of them

        ## Solution 2: time O(n), space O(1)
        # one pass iteration - buy dip sell high
        # e.g [7, 1, 5, 3, 6, 4]
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            buy = min(buy, prices[i-1])
            sell = prices[i]
            profit = max(profit, sell - buy)
        return profit
