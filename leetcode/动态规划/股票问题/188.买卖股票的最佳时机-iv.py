from typing import List
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        for s in range(2, 2 * k+1, 2):
            dp[0][s-1] = - prices[0]
        for j in range(1, len(prices)):
            dp[j][0] = dp[j - 1][0]
            for l in range(2, 2 * k + 1, 2):
                dp[j][l - 1] = max(dp[j - 1][l - 1], dp[j - 1][l - 2] - prices[j])
                dp[j][l] = max(dp[j - 1][l], dp[j - 1][l - 1] + prices[j])
        return dp[-1][-1]

# @lc code=end
