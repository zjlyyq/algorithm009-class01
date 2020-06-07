function myPow(x: number, n: number): number {
    // recursion terminator 
    if (n == 0) return 1.0;
    // prepare data 
    let base: number = n >= 0?1.0:-1.0;
    n = n >= 0?n:-n;
    let ans = 1.0;

    // conquer subproblems 
    let subResult = myPow(x, Math.floor(n/2));

    // process and generate the final result
    ans = n % 2 == 0?subResult*subResult:subResult*subResult*x;

    return base > 0?ans:1/ans;
};


