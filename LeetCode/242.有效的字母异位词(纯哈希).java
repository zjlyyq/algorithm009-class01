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
        HashMap<Character,Integer> cache = new HashMap<Character, Integer>();
        char[] chars = s.toCharArray();
        char[] chart = t.toCharArray();
        for(char c : chars){
            if (cache.get(c) == null) {
                cache.put(c, 1);
                continue;
            }
            int count = cache.get(c);
            cache.replace(c, count, count+1);
        }
        for(char c : chart){
            if (cache.get(c) == null) {
                return false;
            }
            int count = cache.get(c);
            if (count == 1) {
                cache.remove(c);
            }
            else {
                cache.replace(c, count, count-1);
            }
        }
        return cache.isEmpty();
    }
}
// @lc code=end

