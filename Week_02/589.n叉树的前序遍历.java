/*
 * @lc app=leetcode.cn id=589 lang=java
 *
 * [589] N叉树的前序遍历
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        if (root == null) return new ArrayList<Integer>();
        List<Integer> list = new ArrayList<Integer>();
        list.add(root.val);
        for(Node node : root.children) {
            list.addAll(preorder(node));
        }
        return list;
    }
}
// @lc code=end

