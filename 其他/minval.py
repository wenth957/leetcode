class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 有序数组相邻结点一定最小
        self.minval = float('inf')
        self.pre = None

        def traversal(node):
            if not node:
                return
            traversal(node.left)
            if self.pre:
                self.minval = min(self.minval, node.val - self.pre.val)
            self.pre = node
            traversal(node.right)
        traversal(root)
        return self.minval


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(4, TreeNode(2), TreeNode(6))
    print(s.getMinimumDifference(root))
