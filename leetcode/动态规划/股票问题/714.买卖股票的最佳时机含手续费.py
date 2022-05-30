from typing import List
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 买入计算手续费
        dp = [[0, 0]] * len(prices)
        dp[0][0] = - prices[0] - fee
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return max(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(Solution().maxProfit(prices, fee))
# @lc code=end
