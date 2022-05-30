#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def robNode(node):
            if not node:
                return (0, 0)
            left = robNode(node.left)
            right = robNode(node.right)
            val1 = node.val + left[1] + right[1]
            val2 = max(left[0], left[1]) + max(right[0], right[1])
            return (val1, val2)
        res = robNode(root)
        return max(res[0], res[1])

# @lc code=end
