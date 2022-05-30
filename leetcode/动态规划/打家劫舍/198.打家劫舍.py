from typing import List
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
# @lc code=end
