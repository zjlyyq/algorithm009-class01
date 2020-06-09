/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function kthSmallest(matrix, k) {
    var map = new Map();
    var rowSize = matrix[0].length;
    for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < rowSize; j++) {
            if (map.get(matrix[i][j]) == undefined)
                map.set(matrix[i][j], 1);
            else {
                map.set(matrix[i][j], map.get(matrix[i][j]) + 1);
            }
        }
    }
    var mapAsc = [...map.entries()].sort((a,b)=>{return a[0]>=b[0]?1:-1})
    var c = 0;
    for(let i = 0;i < mapAsc.length;i ++) {
        c += mapAsc[i][1];
        if (c > k) return mapAsc[i][0];
    }
    return 0;
}
