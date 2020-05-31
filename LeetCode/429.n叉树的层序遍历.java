import java.util.ArrayList;

/*
 * @lc app=leetcode.cn id=429 lang=java
 *
 * [429] N叉树的层序遍历
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
    public List<List<Integer>> levelOrder(Node root) {
        if (root == null) return new ArrayList<List<Integer>>();
        List<List<Integer>> lists =  new ArrayList<ArrayList<Integer>>();
        dfs(root, lists, 0);
        return lists;
    }
    public void dfs(Node root, List<List<Integer>> lists, Integer layer) {
        if (root == null) return;
        if (lists.length < layer) {
            lists.add(new ArrayList<Integer>());
        }
        lists.get(0).add(root.val);
        for (Node node : root.chuldren) {
            dfs(root, lists, layer + 1);
        }
    }
}
// @lc code=end

