# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = -1 << 30
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(root):
            if root == None:
                return 0
            sum_left_single = dfs(root.left)
            sum_right_single = dfs(root.right)
            t_single = t = root.val
            if sum_left_single > 0:
                t += sum_left_single
            if sum_right_single > 0:
                t += sum_right_single
            max_single = sum_left_single
            if sum_left_single < sum_right_single:
                max_single = sum_right_single
            if max_single > 0:
                t_single += max_single
            if t > self.ans:
                self.ans = t
            return t_single
        dfs(root)
        return self.ans

