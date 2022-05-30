from typing import List
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        if dp[amount] > amount + 2:
            return -1
        return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))
# @lc code=end
