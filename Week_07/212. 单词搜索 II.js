/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
class Trie {
    constructor() {
        this.nextLevel = [];
    }
    /**
     * @param {string} word 
     * @return {void}
     */
    insert(word) {
        let level = this.nextLevel;
        for(let c of word){
            if (level[c] === void 0) {
                level[c] = new Trie();
            }
            level = level[c];
        }
        level["#"] = true;
    }

    /**
     * @param {string} word 
     * @return {bollean}
     */
    search(word) {
        let level = this.nextLevel;
        for(let c of word){
            if (level[c] === void 0) {
                return false;
            }
            level = level[c];
        }
        return level["#"] != undefined;
    }
    
    /**
     * 
     * @param {string} word
     * @return {bollean} 
     */
    startsWith(word) {
        let level = this.nextLevel;
        for(let c of word){
            if (level[c] === void 0) {
                return false;
            }
            level = level[c];
        }
        return true;
    }
}
let trie = new Trie();
let wordSet = new Map();
let x_range = 0;
let y_range = 0; 
let dx = [0, 1, 0, -1];
let dy = [1, 0, -1, 0];
var findWords = function(board, words) {
    // 构建字典树
    for (let word of words) {
        trie.insert(word);
    }
    x_range = board[0].length;
    y_range = board.length;

    for(let i = 0;i < y_range;i ++) {
        for (let j = 0;j < x_range;j ++) {
            dfs("", j, i, board);
        }
    }

    let ans = [];
    for(let [key, value] of wordSet) {
        ans.push(key);
    }
    return ans;
};

var dfs = function (word, x, y, board) {
    if (x < 0 || x >= x_range || y < 0 || y >= y_range) return;
    word += board[y][x];
    if (!trie.startsWith(word)) return;
    if (trie.search(word)) {
        wordSet.set(word, true);
    } 
    for (let i = 0;i < 4;i ++) {
        dfs(word, x+dx[i], y+dy[i], board);
    }
}
