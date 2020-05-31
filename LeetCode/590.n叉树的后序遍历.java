import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=590 lang=java
 *
 * [590] N叉树的后序遍历
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
    public List<Integer> postorder(Node root) {
        if (root == null) return new ArrayList<Integer>();
        List<Integer> list = new ArrayList<Integer>();
        for(Node node : root.children) {
            list.addAll(postorder(node));
        }
        list.add(root.val);
        return list;
    }
}
// @lc code=end

