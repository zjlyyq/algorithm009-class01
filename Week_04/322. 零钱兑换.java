class Solution {
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        int[] ans = new int[1];
        ans[0] = 1<<31 - 1;
        dfs(amount, coins, coins.length-1, 0, ans);
        return ans[0] == 1<<31 -1?-1:ans[0];
    }
    public void dfs(int amount,int[] coins, int c_index, int times, int[] ans) {
        if (amount == 0) {
            ans[0] = Math.min(ans[0], times);
        }
        if (c_index < 0) return;
        int k = amount / coins[c_index];
        for (int i = k;i >= 0 && k + times < ans[0] ;i --) {
            dfs(amount-coins[c_index]*i, coins, c_index-1, times+i, ans);
        }
    }
}