/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {string} S
 * @return {TreeNode}
 */
var recoverFromPreorder = function(S) {
    if (S == "") return null;
    var stack = [];
    var root = new TreeNode();
    var tuple = getNextNodeInfo(S);
    var cur_deepth = tuple[1];
    var cur_val = parseInt(tuple[0]);
    root.val = cur_val;
    stack.push([root, cur_deepth]);
    S = S.substring(tuple[0].length + tuple[1]);
    while (S) {
        tuple = getNextNodeInfo(S);
        cur_deepth = tuple[1];
        cur_val = parseInt(tuple[0]);
        var cur_node = new TreeNode();
        cur_node.val = cur_val;
        while (stack[stack.length - 1][1] != (cur_deepth - 1)) {
            stack.pop();
        }
        var parent_1 = stack[stack.length - 1][0];
        if (!parent_1.left) {
            parent_1.left = cur_node;
        }
        else {
            parent_1.right = cur_node;
        }
        stack.push([cur_node, cur_deepth]);
        S = S.substring(tuple[0].length + tuple[1]);
    }
    return root;
}
function getNextNodeInfo(s) {
    var deepth = 0;
    var stringValue = "";
    for (var i = 0; i < s.length; i++) {
        if (s[i] != "-") {
            break;
        }
    }
    deepth = i;
    s = s.substring(i);
    var index = s.indexOf("-");
    if (index == -1) {
        stringValue = s;
    }
    else {
        stringValue = s.substring(0, index);
    }
    return [stringValue, deepth];
}
