import java.sql.Array;
import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=974 lang=java
 *
 * [974] 和可被 K 整除的子数组
 */

// @lc code=start
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] cache = new int[K];
        int sum = 0;
        int ans = 0,mod = 0;
        cache[0] = 1;
        for (int i = 0; i < A.length; i ++){
            sum += A[i];
            mod = sum%K;
            mod = mod < 0?mod + K:mod; //java的负数取模是负数
            if (cache[mod] ++ == 0) continue;
            ans += cache[mod] - 1;
        }
        return ans;
    }
}
// @lc code=end

