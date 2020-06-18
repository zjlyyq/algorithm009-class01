/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    queue = [root]
    nextLevel = []
    ans = []
    while(queue.length) {
        len = queue.length;
        while(len --) {
            cur = queue.shift()
            if(cur) {
                ans[ans.length] = cur.val
                nextLevel[nextLevel.length] = cur.left
                nextLevel[nextLevel.length] = cur.right
            }
            else {
                ans[ans.length] = null
            }
        }
    }
    while(!ans[ans.length-1]){
        ans.pop()
    }
    return JSON.stringify(ans)
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    list = JSON.parse(data);
    if(list.length == 0) return null
    let root = new TreeNode();
    root.val = list.shift()
    queue = []
    queue[queue.length] = root;

    while(queue.length > 0) {
        cur = queue.shift()
        if (!cur) continue
        if (list.length > 0) {
            let t = list.shift();
            if (t) {
                let left = new TreeNode()
                left.val = list.shift()
                cur.left = left
            }
            if (list.length > 0) {
                let t = list.shift();
                if (t) {
                    let right = new TreeNode()
                    right.val = list.shift()
                    cur.right = right
                }
            }
        }
        queue[queue.length] = cur.left
        queue[queue.length] = cur.right
    }
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */