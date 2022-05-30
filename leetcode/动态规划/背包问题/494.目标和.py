from typing import List
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        if target > sum_ or target < - sum_:
            return 0
        if (sum_ + target) % 2 != 0:
            return 0
        left_ = int((sum_ + target) / 2)
        dp = [0] * (left_ + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(left_, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[left_]


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    s = Solution()
    l = s.findTargetSumWays(nums, target)
    print(l)

# @lc code=end
