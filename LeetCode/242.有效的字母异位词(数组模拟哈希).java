import java.sql.Array;
import java.util.HashMap;

import jdk.nashorn.internal.IntDeque;

/*
 * @lc app=leetcode.cn id=242 lang=java
 *
 * [242] 有效的字母异位词
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] counts = new int[26];
        for(int i = 0;i < s.length();i ++) {
            counts[s.charAt(i) - 'a'] ++;
            counts[t.charAt(i) - 'a'] --;
        }
        for (int i = 0;i < counts.length; i ++) {
            if (counts[i] != 0) return false;
        }
        // for (int count : counts) {
        //     if (count != 0) return false;
        // }
        return true;
    }
}
// @lc code=end

