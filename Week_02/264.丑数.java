class Solution {
    
    public int nthUglyNumber(int n) {
        int count = 1;
        int[] dp = new int[3];
        int[] yinzi = new int[] {2, 3, 5};
        dp[0] = dp[1] = dp[2] = 0;
        int[] ans = new int[n];
        ans[0] = 1;
        while(count < n) {
            int pos = minPosFromThree(2*ans[dp[0]], 3*ans[dp[1]], 5*ans[dp[2]]);
            if (ans[dp[pos]]*yinzi[pos] > ans[count-1]) ans[count++] = ans[dp[pos]]*yinzi[pos];
            dp[pos]++ ;
        }
        return ans[n-1];
    }

    public int minPosFromThree(int a, int b, int c) {
        if (a <= b && a <= c) return 0;
        if (b <= a && b <= c) return 1;
        if (c <= b && c <= a) return 2;
        return -1;
    }
}