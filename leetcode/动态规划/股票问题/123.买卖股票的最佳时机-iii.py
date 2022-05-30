from typing import List
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1] = - prices[0]
        dp[0][3] = - prices[0]
        for i in range(1, len(prices)):
            for j in range(5):
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
                dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
                dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        res = dp[-1][0]
        for j in range(1, 5):
            res = max(res, dp[-1][j])
        return res
# @lc code=end
