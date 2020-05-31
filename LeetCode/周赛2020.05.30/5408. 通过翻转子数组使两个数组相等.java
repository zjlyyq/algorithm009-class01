import java.util.Stack;

class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        int [] count = new int[1001];

        for (int i = 0;i < target.length;i ++) {
            count[target[i]] ++;
            count[arr[i]] --;
        }

        for (int i = 0;i < target.length;i ++) {
            if (count[target[i]] != 0) return false;
        }

        return true;
    }
}