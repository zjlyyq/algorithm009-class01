import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

/*
 * @lc app=leetcode.cn id=51 lang=java
 *
 * [51] N皇后
 */

// @lc code=start
class Solution {
    ArrayList<Integer> sum1 = new ArrayList<>();  //正对角线的和
    ArrayList<Integer> sum2 = new ArrayList<>();  //反对角线的和
    HashSet<Integer> rows = new HashSet<>();  //已占据的行
    HashSet<Integer> cols = new HashSet<>();  //已占据的列
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    List<Integer> tmpList = new ArrayList<Integer>();
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> list = new ArrayList<List<String>>();
        String template = "";
        for (int i = 0;i < n;i ++) template += ".";
        // System.out.println(template);
        backTrack(0,n);
        // System.out.println(ans);
        for(int i = 0;i < ans.size();i ++){
            ArrayList<String> s = new ArrayList<>();
            for (int j : ans.get(i)) {
                String sCopy = template;
                // System.out.println(sCopy);
                char[] c = sCopy.toCharArray();
                c[j] = 'Q';
                // System.out.println(c);
                // sCopy = ;
                s.add(String.valueOf(c));
            }
            list.add(s);
        }
        return list;
    }
    public void backTrack(int row, int n) {
        for (int col = 0; col < n; col ++){
            if (cols.contains(col)) continue;
            int flag = 1;
            for (int j = 0;j < sum1.size(); j ++){
                if ((row+col) == sum1.get(j) || (row-col) == sum2.get(j)) {
                    flag = 0;
                    break;
                }
            }
            if (flag == 1) {
                // System.out.println('s');
                tmpList.add(col);
                // System.out.println(tmpList);
                if (row == n-1){
                    ans.add(new ArrayList<>(tmpList));
                    tmpList.remove((Object)(col));
                }
                else if (row < n-1){
                    cols.add(col);
                    sum1.add(row + col);
                    sum2.add(row - col);
                    // System.out.println(sum1);
                    // System.out.println(sum2);
                    // System.out.println(cols);
                    backTrack(row+1, n);
                    sum1.remove((Object)(row+col));
                    sum2.remove((Object)(row - col));
                    cols.remove(col);
                    tmpList.remove((Object)(col));
                } 
            }
        }
    }
}
// @lc code=end

