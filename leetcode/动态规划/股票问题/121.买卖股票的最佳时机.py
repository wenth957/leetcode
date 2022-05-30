from typing import List
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(-prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
        return max(dp[-1][0], dp[-1][1])


if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(nums))

# @lc code=end
