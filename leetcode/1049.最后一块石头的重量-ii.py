from typing import List
#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_ = sum(stones)
        v = sum_ // 2
        dp = [0] * (1 + v)
        for i in range(len(stones)):
            for j in range(v, stones[i] - 1, -1):
                dp_0 = dp[j]
                dp_1 = dp[j - stones[i]] + stones[i]
                dp[j] = max(dp_0, dp_1)
        return sum_ - 2 * dp[v]


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    s = Solution()
    print(s.lastStoneWeightII(stones))
# @lc code=end
