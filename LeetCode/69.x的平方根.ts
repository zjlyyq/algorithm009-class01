function mySqrt(x: number): number {
    return binary_search(1, x, x)
};
function binary_search(l:number, r: number, x: number): number {
    // 二分查找第一个平方比x大的数
    while(l <= r) {
        let mid: number = Math.floor((l + r)/2);
        if (mid*mid == x){
            return mid;
        }
        else if(mid*mid < x) {
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
    }
    return l-1;
}