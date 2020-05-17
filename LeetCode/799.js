// /**
//  * @param {number} poured
//  * @param {number} query_row
//  * @param {number} query_glass
//  * @return {number}
//  */
// var champagneTower = function(poured, query_row, query_glass) {
//     var arr = [];
//     arr[-1] = 0;
//     arr[0] = 1;
//     var s = 1;
//     while(true) {
//         arr[s] = arr[s-1] + s + 1;
//         if(arr[s] > 1000000000) {
//             break;
//         }
//         s ++;
//     }
//     // 二分查找水流层数
//     var l = 0,r = s;
//     while(l <= r){
//         var mid = parseInt((l+r)/2.0);
//         // console.log(l,mid,r);
//         if (arr[mid] <= poured) {
//             l = mid+1;
//         }else {
//             r = mid-1;
//         }
//         // console.log(l,mid,r);
//         // console.log('--------');
//     }
//     // console.log(l);
//     if (query_row < l) {
//         return '1.0';
//     }else if( query_row == l ){
//         if (poured - arr[l-1] == 0){
//             return '0.0';
//         }
//         return (poured - arr[l-1])/(l+1);
//     }else {
//         return '0.0';
//     }
// };
// console.log(champagneTower(4,2,0))

/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
var champagneTower = function(poured, query_row, query_glass) {
    let lastLay = new Array(44720);
    let array = new Array(44720);
    let tmp = lastLay;
    lastLay[0] = poured;
    for(let lay = 1;lay <= query_row;lay ++){
        for (let j = 0;j <= lay;j ++) {
            if (j == 0) {
                array[j] = lastLay[0]-1 > 0?(lastLay[j]-1)/2:0;
            }else if(j == lay){
                array[j] = (lastLay[j-1]-1>0?(lastLay[j-1]-1)/2.0:0);
            }else {
                array[j] = (lastLay[j-1]-1>0?(lastLay[j-1]-1)/2.0:0) + (lastLay[j]-1>0?(lastLay[j]-1)/2.0:0);
            }
        }
        // console.log(array);
        tmp = array;
        array = lastLay;
        lastLay = tmp;
    }
    // console.log(tmp[query_glass]);
    return tmp[query_glass] > 1?1:tmp[query_glass];
};
console.log(champagneTower(2,0,0));

