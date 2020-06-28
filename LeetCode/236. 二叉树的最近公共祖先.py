# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            if root == None:
                return False
            lson = dfs(root.left, p , q)
            rson = dfs(root.right, p, q)
            if lson and rson or ((lson or rson) and (root.val == p.val or root.val == q.val)):
                self.ans = root
            if lson or rson or (root.val == p.val or root.val == q.val):
                return True
            return False
        dfs(root, p, q)

        return self.ans