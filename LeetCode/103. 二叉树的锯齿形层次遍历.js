/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    if (root == null) return [];
    let queue = [];
    queue.push(root)
    ans = []
    count = 0;
    while(queue.length > 0) {
        let queuq_size = queue.length;
        let level = []
        for (let i = 0;i < queuq_size; i++) {
            let cur = queue.shift()
            if (count % 2) {
                level = [cur.val].concat(level)
            }
            else {
                level.push(cur.val)
            }
            if (cur.left) queue.push(cur.left)
            if (cur.right) queue.push(cur.right)
        }
        count ++;
        ans.push(level)
    }

    // for (let i = 0;i < ans.length;i ++) {
    //     if (i % 2) {
    //         ans[i] = ans[i].reverse()
    //     }
    // }
    return ans;
};