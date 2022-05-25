from typing import List
#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            v = total // 2
        dp = [0] * (v + 1)
        for i in range(len(nums)):
            for j in range(v, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        if dp[-1] == v:
            return True

        return False


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    s = Solution()
    print(s.canPartition(nums))
# @lc code=end
