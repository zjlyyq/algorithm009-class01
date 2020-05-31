import java.util.LinkedList;

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) return new ArrayList<Integer>(); 
        Stack<TreeNode> stack = new Stack<>();
        LinkedList<Integer> list = new LinkedList<Integer>();
        TreeNode curNode = root;
        stack.push(curNode);
        while (!stack.isEmpty()) {
            curNode = stack.pop();
            list.addFirst(curNode.val);
            if (curNode.left != null) {
                stack.push(curNode.left)
            }
            if (curNode.right != null) {
                stack.push(curNode.right)
            }
        }
        return list;
    }
}