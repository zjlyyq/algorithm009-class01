import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=78 lang=java
 *
 * [78] 子集
 */

// @lc code=start
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        list.add(new ArrayList<Integer>());
        for(int i : nums){
            int listLength = list.size();
            for(int j = 0;j < listLength;j ++) {
                ArrayList<Integer> tList = new ArrayList<Integer>(list.get(j));
                tList.add(i);
                list.add(tList);
            }
        }
        return list;
    }
}
// @lc code=end

