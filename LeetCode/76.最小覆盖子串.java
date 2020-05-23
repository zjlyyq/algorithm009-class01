/*
 * @lc app=leetcode.cn id=76 lang=java
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
class Solution {
    public String minWindow(String s, String t) {
        char [] sCharArray = s.toCharArray();
        char [] tCharArray = t.toCharArray();
        // 字符频数数组
        int [] sFreq = new int[128];
        int [] tFreq = new int[128];
        // System.out.println(sFreq[100]);
        for(char c : tCharArray){
            tFreq[c] ++;
        }
        int l = 0,r = 0;
        int distance = 0;
        int minLen = s.length() + 1;
        int start = 0;
        while(r < s.length()) {
            char c = sCharArray[r];
            if (tFreq[c] == 0) {
                r ++;
                continue;
            }
            sFreq[c] ++;
            if (tFreq[c] > (sFreq[c]-1)) distance ++;
            if (distance == t.length()) {
                while(l <= r && distance == t.length()){
                    char z = sCharArray[l];
                    if (tFreq[z] == 0) {
                        l ++;
                        continue;
                    }
                    l ++;
                    sFreq[z] --;
                    if (tFreq[z] > sFreq[z]) distance --;
                }
                if ((r-l+2) < minLen) {
                    minLen = r-l+2;
                    start = l-1;
                }
            }
            r ++;
        }
        if (minLen > s.length()) return "";
        return s.substring(start, start+minLen);
    }
}
// @lc code=end

