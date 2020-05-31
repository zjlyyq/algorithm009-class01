import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> list = new ArrayList<List<String>>();
        for (String s : strs) {
            int i = 0;
            for (i = 0;i < list.size();i ++) {
                if (list.get(i).get(0).length() != s.length()) continue;
                if (isAnagram(list.get(i).get(0), s)) {
                    list.get(i).add(s);
                    break;
                }
            }
            if (i == list.size()){
                List<String> tmpList = new ArrayList<String>();
                tmpList.add(s);
                list.add(tmpList);
            }
        }
        return list;
    }
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
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

