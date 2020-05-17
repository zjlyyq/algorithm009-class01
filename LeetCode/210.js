/**
 * @param {number} numCourses 
 * @param {number[][]} prerequisites 
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    // 节点出度入度表
    var inOutGraph = [];
    for(let i = 0;i < numCourses;i ++) {
        inOutGraph.push(
            {
                inDeg:0,
                outDeg:0,
                visited: false
            }
        )
    }

    prerequisites.forEach(item  => {
        let a = item[0],b = item[1];
        inOutGraph[a].inDeg ++;
        inOutGraph[b].outDeg ++;
    })
    
    let ans = []
    let startNode = -1;
    for (let i = 0;i < numCourses;i ++) {
        if (inOutGraph[i].inDeg == 0){
            startNode = i;
            inOutGraph[i].visited = true;
            ans.push(i);
            break;
        }
    }

    while(true && startNode >= 0 && ans.length < numCourses){
        prerequisites.forEach(item => {
            if (item[1] == startNode) {
                inOutGraph[item[0]].inDeg --;
            }
        })
        startNode = -1;
        for(let i = 0;i < numCourses;i ++){
            if (inOutGraph[i].inDeg == 0 && !inOutGraph[i].visited){
                startNode = i;
                ans.push(i);
                inOutGraph[i].visited = true;
                break;
            }
        }
    }

    return ans.length == numCourses?ans:[];
};

console.log(findOrder(3,[[1,0],[1,2],[0,1]]));