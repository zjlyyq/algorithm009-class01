import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.Queue;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=94 lang=java
 *
 * [94] 二叉树的中序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) return new ArrayList<Integer>(); 
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> list = new ArrayList<Integer>();
        stack.push(root);
        // 记录节点是否进过栈
        HashMap<TreeNode, Integer> cache = new HashMap<TreeNode, Integer>();
        while (!stack.isEmpty()) {
            TreeNode treeNode = stack.pop();
            if ( treeNode.right != null && cache.get(treeNode.right) == null) {
                stack.push(treeNode.right);
                cache.put(treeNode.right, 1);
                stack.push(treeNode);
                if (treeNode.left != null && cache.get(treeNode.left) == null) {
                    stack.push(treeNode.left);
                    cache.put(treeNode.left, 1);
                }
                continue;
            }
            if (treeNode.left != null && cache.get(treeNode.left) == null) {
                stack.push(treeNode);
                stack.push(treeNode.left);
                // 加这行和在打印的时候加一样
                cache.put(treeNode.left, 1);
                continue;
            }
            list.add(treeNode.val);
            // 加这行和在打印的时候加一样
            // cache.put(treeNode, 1);
        }
        return list;
    }
}
// @lc code=end

