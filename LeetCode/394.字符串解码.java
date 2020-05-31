import java.util.Stack;

/*
 * @lc app=leetcode.cn id=394 lang=java
 *
 * [394] 字符串解码
 */

// @lc code=start
class Solution {
    public String decodeString(String s) {
        Stack<String> stack1 = new Stack<String>();
        Stack<Integer> stack2 = new Stack<>();
        String ans = "";
        char[] charArray = s.toCharArray();
        String num = "";
        String targetStr = "";
        for(char c:charArray) {
            if (c >= '0' && c <= '9') {
                num += c;
                continue;
            }
            if (c == '[') {
                stack1.push(""+c);
                stack2.push(Integer.parseInt(num));
                stack1.push(targetStr);
                num = "";
                targetStr = "";
                continue;
            }
            if (c == ']') {
                targetStr = "";
                while(!(stack1.peek()).equals("[") ) {
                    targetStr = stack1.pop() + targetStr;
                }
                stack1.pop();
                String t = getDStr(targetStr, stack2.pop());
                stack1.push(t);
                continue;
            }
            targetStr += c;
            num = "";
        }
        while(!stack1.isEmpty()){
            ans = stack1.pop()+ans;
        }
        return ans;

    }
    public String getDStr(String s, int n) {
        String ret = "";
        while(n -- > 0) {
            ret += s;
        }
        return ret;
    }

}
// @lc code=end

