#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        begin = 0
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] != s[j]:
                    continue
                elif j - i < 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                # 所有回文子串
                if dp[i][j] and res < j - i + 1:
                    res = j - i + 1
                    begin = i
        return s[begin:begin + res]

# @lc code=end
