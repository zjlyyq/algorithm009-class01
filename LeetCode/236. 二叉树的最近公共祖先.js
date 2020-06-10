/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
let pathP = []
let pathQ = []
var lowestCommonAncestor = function(root, p, q) {
    dfs(root, q, pathQ);
    dfs(root, p, pathP);
    for (let i = pathP.length - 1, j = pathQ.length - 1;i >= 0&&j >= 0;i --,j --){
        if (pathP[i] != pathQ[j]) return pathP[i+1]
    }
    return pathP.length < pathQ.length?pathP[0]:pathQ[0];
};

function dfs(root, target, path) {
    if (root == target) return path.push(root);
    if (root == null) return false;
    if ( dfs(root.left, target, path) || dfs(root.right, target, path)) {
        return path.push(root);
    }
    return false;
}