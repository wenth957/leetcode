from typing import List
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) - 1)
        if len(nums) == 1:
            return nums[0]

        def robrange(left, right):
            dp[0] = nums[left]
            if right - left == 1:
                return dp[0]
            dp[1] = max(nums[left], nums[left + 1])
            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[left + i])
            return dp[-1]
        nohead = robrange(1, len(nums))
        notail = robrange(0, len(nums) - 1)
        return max(nohead, notail)


if __name__ == "__main__":
    nums = [0]
    print(Solution().rob(nums))
# @lc code=end
