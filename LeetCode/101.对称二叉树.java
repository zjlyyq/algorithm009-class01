import java.util.ArrayList;

class Solution {
    public boolean isSymmetric(TreeNode root) {
        List<List<Integer>> list = levelOrder(root);
        for (int i = 0;i < list.size();i ++) {
            if (!isSymmetricArray(list.get(i))) return false;
        }
        return true;
    }
    public boolean isSymmetricArray(List<Integer> list) {
        for (int i = 0;i < list.size();i ++) {
            if (list.get(i) != list.get(list.size() - i -1)) return false;
        }
        return true;
    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        getLevelNodes(root, list, 0);
        return list;
    }
    public void getLevelNodes(TreeNode root, List<List<Integer>> list, int level) {
        if (list.size() <= level) {
            list.add(new ArrayList<Integer>());
        }
        if (root == null){
            list.get(level).add(-1);
            return;
        }
        list.get(level).add(root.val);
        getLevelNodes(root.left, list, level+1);
        getLevelNodes(root.right, list, level+1);
    }
}