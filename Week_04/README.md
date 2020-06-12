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

### 贪心

在每一步选择中都采取当前状态下的最优解，从而导致全局最优。

> 和动态规划相比，不同之处在于贪心它对每个子问题的解决方案都做出选择，不能回退。动态规划会**保留**以前的运算结果，有回退功能。

贪心可以用于解决一部分最优问题，例如：最小生成树，求哈夫曼编码。一旦一个问题可以用贪心解决，那么贪心法一般都是最好办法。

#### 适用贪心的场景

问题存在**最优子结构**

#### 难点

怎么证明贪心的正确性



