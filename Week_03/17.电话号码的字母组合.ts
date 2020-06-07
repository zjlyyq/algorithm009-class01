
let strings:string[] = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"];
let strs: string[] = [];
function letterCombinations(digits: string): string[] {
    strs = [];
    dfs(digits, 0, ""); 
    return strs;
};

function dfs(digits: string, level: number, str: string): void {
    if (level == digits.length) {
        strs.push(str);
        return;
    }

    let dig: number = parseInt(digits[level]);
    let ss: string = strings[dig-2];
    for (let i = 0; i < ss.length; i ++) {
        dfs(digits, level + 1, str+ss[i]);
    }
}

