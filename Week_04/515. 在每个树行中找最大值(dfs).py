# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res, 0)
        return res

    def dfs(self, root, res, level):
        if root == None: return
        if len(res) >= level+1: res[level] = max(res[level], root.val)
        else: res.append(root.val)
        self.dfs(root.left, res, level + 1)
        self.dfs(root.right, res, level + 1)