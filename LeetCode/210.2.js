/**
 * @param {number} numCourses 
 * @param {number[][]} prerequisites 
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    // 节点入度表
    let indeg = [];
    // 单向边
    let edges = [];
    // 数组模拟队列
    let queue = [], queueIndex = 0;
    // 拓扑排序结果
    let ans = []

    for(let i = 0;i < numCourses;i ++) {
        indeg.push(0);
        edges.push([])
    }

    prerequisites.forEach(item  => {
        let a = item[0], b = item[1];
        indeg[a] ++;
        edges[b].push(a);
    })
    
    for (let i = 0; i < numCourses; i ++) {
        if (indeg[i] == 0){
            queue.push(i);
            ans.push(i);
        }
    }
    while(queue && queueIndex < queue.length) {
        let startNode = queue[queueIndex];
        for(let i = 0; i < edges[startNode].length; i ++) {
            let b = edges[startNode][i];
            if (--indeg[b] == 0) {
                queue.push(b);
                ans.push(b);
            }
        }
        queueIndex ++;
    }
    return ans.length == numCourses ? ans : [];
};

console.log(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]));