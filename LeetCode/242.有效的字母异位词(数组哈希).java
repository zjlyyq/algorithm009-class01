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
        int[] size = new int[26];
        char[] chars = s.toCharArray();
        char[] chart = t.toCharArray();
        for(char c : chars){
            size[c-'a'] ++;
        }
        for(char c : chart){
            size[c-'a'] --;
        }
        for(int i = 0;i < 26;i ++) {
            if (size[i] != 0) return false;
        }
        return true;
    }
}
// @lc code=end

