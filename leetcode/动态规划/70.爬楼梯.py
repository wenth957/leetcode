#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 每次可以爬m层楼梯 m个物品，装满n层楼梯
        m = 2
        dp = [0] * (n + 1)
        dp[0] = 1
        for j in range(n + 1):
            for i in range(1, m + 1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[n]


if __name__ == "__main__":
    n = 3
    print(Solution().climbStairs(n))
# @lc code=end
