import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        if (height.length == 0) return 0;
        int [] leftPos = new int[height.length];
        int [] rightPos = new int[height.length];
        leftPos[0] = -1;
        rightPos[height.length-1] = -1;
        for(int i = 1,j = height.length-2;i < height.length && j > -1;i ++,j--) {
            int prePos = i-1;
            int nextPos = j+1;
            while(true) {
                if (height[prePos] > height[i]) {
                    leftPos[i] = prePos;
                    break;
                }
                else {
                    prePos = leftPos[prePos];
                }
                if (prePos == -1){
                    leftPos[i] = -1;
                    break;
                }
            }
            while(true) {
                if (height[nextPos] > height[j]) {
                    rightPos[j] = nextPos;
                    break;
                }
                else {
                    nextPos = rightPos[nextPos];
                }
                if (nextPos == -1){
                    rightPos[j] = -1;
                    break;
                }
            }
        }
        int ans = 0;
        HashMap<String,Boolean> hashMap = new HashMap<>();
        for (int i = 0;i < height.length;i ++){
            if (leftPos[i] == -1 || rightPos[i] == -1) continue;
            int a = leftPos[i];
            int b = rightPos[i];
            String s = Integer.toString(a) + Integer.toString(b);
            if (hashMap.get(s) != null) continue;
            hashMap.put(s, true);
            int w = ((rightPos[i]-leftPos[i])-1);
            int h = Math.min(height[leftPos[i]], height[rightPos[i]])-height[i];
            ans += w*h;
        }
        return ans;
    }
}
// @lc code=end

