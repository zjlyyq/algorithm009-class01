### 图论
#### 图的表示(以无向图为例)
1. 邻接表

   ```java
   public class Graph { // 无向图
     private int v; // 顶点的个数
     private LinkedList<Integer> adj[]; // 邻接表
   
     public Graph(int v) {
       this.v = v;
       adj = new LinkedList[v];
       for (int i=0; i<v; ++i) {
         adj[i] = new LinkedList<>();
       }
     }
   
     public void addEdge(int s, int t) { // 无向图一条边存两次
       adj[s].add(t);
       adj[t].add(s);
     }
   ```

2. 邻接矩阵

   ```
   
   ```

#### 深度优先遍历

1. 携带层数信息
2. 进入到下层前将当前节点置为: `visited: true`
3. 回溯：当前节点访问信息恢复为：`visited: false`

#### 广度优先遍历



