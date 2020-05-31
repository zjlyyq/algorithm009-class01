import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    ArrayList<ArrayList<Integer>> routers = new ArrayList<ArrayList<Integer>>();  //保存原路径的反向
    ArrayList<ArrayList<Integer>> routersBack = new ArrayList<ArrayList<Integer>>(); //保存原路径的反向的反向，两个数组构成无向图信息
    Queue<Integer> q = new LinkedList<Integer>();
    int [] route;
    int ans = 0;
    
    public int minReorder(int n, int[][] connections) {
        boolean[] visited = new boolean[n];
        // 数组初始化
        for (int i = 0;i < n;i ++) {
            routers.add(new ArrayList<Integer>());
            routersBack.add(new ArrayList<Integer>());
        }
        for (int i = 0;i < connections.length;i ++) {
            route = connections[i];
            routers.get(route[1]).add(route[0]);
            routersBack.get(route[0]).add(route[1]);
        }
        q.add(0);
        visited[0] = true;
        while(!q.isEmpty()) {
            int cur = q.poll();
            ArrayList<Integer> r = routers.get(cur);
            for (int i = 0;i < r.size();i ++) {
                int endNode = r.get(i);
                if (visited[endNode] != true) {
                    visited[endNode] = true;
                    q.add(endNode);
                }
            }
            r = routersBack.get(cur);
            for (int i = 0;i < r.size();i ++) {
                int endNode = r.get(i);
                if (visited[endNode] != true) {
                    visited[endNode] = true;
                    q.add(endNode);
                    ans ++;
                }
            } 
        }

        return ans;
     }
}