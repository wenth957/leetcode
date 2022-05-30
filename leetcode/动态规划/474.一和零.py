from typing import List
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for str_ in strs:
            count_0, count_1 = 0, 0
            for s in str_:
                if s == '0':
                    count_0 += 1
                else:
                    count_1 += 1
            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    last_max = dp[i - count_0][j - count_1]
                    dp[i][j] = max(dp[i][j], last_max + 1)
        return dp[-1][-1]


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    s = Solution()
    print(s.findMaxForm(strs, m, n))

# @lc code=end
