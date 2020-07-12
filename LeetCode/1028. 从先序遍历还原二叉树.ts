
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}



function recoverFromPreorder(S: string): TreeNode | null {
    let stack: [TreeNode, number][] = [];
    let root: TreeNode = new TreeNode();
    let tuple = getNextNodeInfo(S);
    let cur_deepth: number = tuple[1];
    let cur_val: number =  parseInt(tuple[0]);
    root.val = cur_val;
    stack.push([root, cur_deepth])
    S = S.substring(tuple[0].length + tuple[1]);
    while (S) {
        tuple = getNextNodeInfo(S);
        cur_deepth = tuple[1];
        cur_val = parseInt(tuple[0]);
        let cur_node = new TreeNode();
        cur_node.val = cur_val;
        while (stack[stack.length -1][1] != cur_deepth - 1) {
            stack.pop();
        }
        let parent = stack[stack.length - 1][0];
        if (!parent.left) {
            parent.left = cur_node;
        }else {
            parent.right = cur_node;
        }
        stack.push([cur_node, cur_deepth]);
        S = S.substring(tuple[0].length + tuple[1]);
    }
    return root;
};

function getNextNodeInfo(s: string): [string, number] | null {
    let deepth = 0;
    let stringValue = ""
    for (var i = 0; i < s.length; i++) {
        if (s[i] != "-") {
            break;
        }
    }
    deepth = i;
    s = s.substring(i);
    let index = s.indexOf("-");
    if (index == -1) {
        stringValue = s;
    } else {
        stringValue = s.substring(0, index);
    }
    return [stringValue, deepth]
}