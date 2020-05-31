import java.sql.Array;

/*
 * @lc app=leetcode.cn id=974 lang=java
 *
 * [974] 和可被 K 整除的子数组
 */

// @lc code=start
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int [][] a = new int[2][K];
        int ans = 0;
        int mod;
        for (int i = 1;i <= A.length;i ++) {
            if (A[i-1]%K == 0) {
                System.arraycopy(a[(i-1)%2], 0, a[i%2], 0, K);
                mod = (A[i-1]+K)%K;
                mod = mod < 0? mod+K : mod;
                a[i%2][mod] ++;
                ans += a[i%2][0];
                continue;
            }
            for (int j = 0;j < K;j ++) {
                mod = (j+A[i-1])%K;
                mod = mod < 0? mod+K : mod;
                a[i%2][mod] = a[(i-1)%2][j];
            }
            mod = (A[i-1]+K)%K;
            mod = mod < 0? mod+K : mod;
            a[i%2][mod] ++;
            ans += a[i%2][0];
        }
        // System.out.print((-5)%5);
        return ans;
    }
}
// @lc code=end

