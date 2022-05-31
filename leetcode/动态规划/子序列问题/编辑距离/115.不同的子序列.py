#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            # 任意字符串都能匹配一次0字符串
            dp[i][0] = 1
            for j in range(1, n + 1):
                # 0 字符串不能匹配其他字符串
                dp[0][j] = 0
                if s[i - 1] == t[j - 1]:
                    # 匹配次数并不增减还是维持原来的路径
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
# @lc code=end
