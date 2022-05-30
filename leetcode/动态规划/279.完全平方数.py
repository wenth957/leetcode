# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n+1):
            for j in range(i**2, n+1):
                dp[j] = min(dp[j], dp[j-i**2]+1)
        return dp[n]
if __name__ == "__main__":
    print(Solution().numSquares(12))
# @lc code=end

