from typing import List
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        dp = [1] * (len(nums))
        dp[0] = 1
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res


# if __name__ == "__main__":
#     while True:
#         s = input()
#         if s != "":
#             nums = list(map(int, s.split()))
#         else:
#             break
#     print(Solution().lengthOfLIS(nums))
# @lc code=end
