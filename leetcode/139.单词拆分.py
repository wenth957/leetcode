from typing import List
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                # 子字符串长度(体积)>= 物品长度 所有满足条件的子串进行比对
                if i >= len(word):
                    # 只要有一个单词在即可 所以放入dp[i] 不同单词间实现
                    dp[i] = (
                        dp[i] or
                        dp[i - len(word)] and
                        s[i - len(word):i] == word)
        return dp[-1]


if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    solve = Solution()
    print(solve.wordBreak(s, wordDict))

    # @lc code=end
