import java.util.Stack;

class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] ans = new int[T.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0;i < T.length;i ++) {
            while (!stack.isEmpty() && T[stack.peek()] < T[i]) {
                ans[stack.peek()] = i - stack.pop();
            }
            stack.push(i);
        }
        return ans;
    }
}