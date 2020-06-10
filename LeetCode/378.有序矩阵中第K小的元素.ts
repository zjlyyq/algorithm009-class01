function kthSmallest(matrix: number[][], k: number): number {
    // 哈希法喽，Js的Map是自带有序的】
    let map:Map<number,number> = new Map();
    let rowSize = matrix[0].length;
    for(let i = 0;i < matrix.length;i ++) {
        for(let j = 0;j < rowSize;j ++) {
            if (map.get(matrix[i][j]) == undefined) map.set(matrix[i][j], 1);
            else {
                map.set(matrix[i][j], map.get(matrix[i][j])+1);
            }
        }
    }
    let c: number = 0;
    for(let [k,v] of map) {
        c += v;
        if (c >= k) return k;
    }
    return 0;
};




