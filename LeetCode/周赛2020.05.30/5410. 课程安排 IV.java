import java.sql.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public List<Boolean> checkIfPrerequisite(int n, int[][] prerequisites, int[][] queries) {
        int[] indegs = new int[n];
        int[] outdegs = new int[n];
        boolean[] exist = new boolean[n];
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        for (int i = 0;i < n;i ++) list.add(new ArrayList<Integer>());
        int a, b;
        for (int i = 0;i < prerequisites.length;i ++) {
            indegs[prerequisites[i][1]] ++;
            outdegs[prerequisites[i][0]] ++;
            a = prerequisites[i][0];
            b = prerequisites[i][1];
            exist[a] = exist[b] = true;
            list.get(a).add(b);
        }
        Queue <Integer> queue = new LinkedList<Integer>();

        for(int i = 0;i < n;i ++) {
            if (indegs[i] == 0 && exist[i]) {
                queue.add(i);
            }
        }
        int[] pos = new int[n];
        int posIndex = 1;
        while(!queue.isEmpty()) {
            int aa = queue.poll();
            if (aa == -1){
                posIndex ++;
                continue;
            }
            pos[aa] = posIndex;
            for(int i = 0;i < list.get(aa).size();i ++) {
                int bb = list.get(aa).get(i);
                indegs[bb] --;
                if (indegs[bb] == 0) {
                    queue.add(-1);
                    queue.add(bb);
                }
            }
        }

        List<Boolean> ans = new ArrayList<Boolean>();

        for (int i = 0;i < queries.length;i ++) {
            if (pos[queries[i][0]] < pos[queries[i][1]] && pos[queries[i][1]] != 0 && pos[queries[i][0]] != 0) {
                ans.add(true);
                continue;
            }
            ans.add(false);
        }
        return ans;
    }
}