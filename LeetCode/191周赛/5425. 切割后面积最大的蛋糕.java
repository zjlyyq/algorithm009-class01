import java.lang.reflect.Array;
import java.util.Arrays;

class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        long maxH, maxW;
        if (horizontalCuts.length == 0) maxH = (long)h;
        else {
            Arrays.sort(horizontalCuts);
            maxH = (long)horizontalCuts[0];
            for (int i = 1;i < horizontalCuts.length;i ++) maxH = Math.max(maxH, (long)(horizontalCuts[i]-horizontalCuts[i-1]));
            maxH = Math.max(maxH, (long)(h-horizontalCuts[horizontalCuts.length-1]));
        }
        if (verticalCuts.length == 0) maxW = (long)w;
        else {
            Arrays.sort(verticalCuts);
            maxW = (long)verticalCuts[0];
            for (int i = 1;i < verticalCuts.length;i ++) maxW = Math.max(maxW, (long)(verticalCuts[i]-verticalCuts[i-1]));
            maxW = Math.max(maxW, (long)(w-verticalCuts[verticalCuts.length-1]));
        }

        return (int)((maxH*maxW)%(long)(1<<9+7));
    }
}