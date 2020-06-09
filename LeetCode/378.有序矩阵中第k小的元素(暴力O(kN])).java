/*
 * @lc app=leetcode.cn id=378 lang=java
 *
 * [378] 有序矩阵中第K小的元素
 */

// @lc code=start
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int ll = matrix.length;
        int lc = matrix[0].length;
        // 矩阵每一行的下标数组
        int [] index = new int[ll];
        int ans = -1;

        while(k -- > 0) {
            int min = (1 << 31) -1;
            System.out.println(min);
            int minIndex = -1;
            for(int i = 0;i < ll;i ++) {
                int j = index[i];
                if (j < lc && matrix[i][j] <= min) {
                    min = matrix[i][j];
                    System.out.println(min);
                    minIndex = i;
                }
            }
            ans = matrix[minIndex][index[minIndex]];
            index[minIndex] ++;
        }

        return ans;
    }
}
// @lc code=end

