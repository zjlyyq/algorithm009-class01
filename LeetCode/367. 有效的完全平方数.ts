function isPerfectSquare(num: number): boolean {
    let l: number  = 1;
    let r: number = num;
    while(l <= r) {
        let mid: number = Math.floor((l+r) / 2)
        if (mid*mid == num) return true;
        else if (mid*mid < num) l = mid + 1;
        else {
            r = mid - 1;
        }
    }
    return false;    
};