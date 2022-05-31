#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                res += dp[i][j]
        return res
# @lc code=end
