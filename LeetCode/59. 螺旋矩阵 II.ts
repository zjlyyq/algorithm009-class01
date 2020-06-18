function generateMatrix(n: number): number[][] {
    // chaek the position 
    function checkPosition2(pos: [number, number], boundary_x: [number, number], boundary_y: [number, number]): boolean {
        if (pos[0] == boundary_x[1] || pos[0] == boundary_x[0]) {
            // console.log(pos);
            return false;
        }
        if (pos[1] == boundary_y[1] || pos[1] == boundary_y[0]) {
            // console.log(pos);
            return false;
        }
        return true;
    }

    if (n == 0) {
        return [];
    }
    let ansMatrix: number[][] = [];
    for (let i = 0;i < n;i ++) {
        let tt: number[] = []
        for (let i = 0;i < n;i ++) {
            tt.push(0)
        }
        ansMatrix.push(tt)
    }
    // 按顺时针定义方向
    let dirs: [number,number][] = [ [0 ,1], [1, 0], [0, -1], [-1, 0] ];
    // 起始位置
    let pos: [number, number] = [0, 0]
    // 起始方向
    let dirIndex:number = 0;
    let boundary_x: [number, number] = [-1,n];
    let boundary_y: [number, number] = [-1,n];
    for(let i = 0;i < n*n;i ++) {
        ansMatrix[pos[0]][pos[1]] = i + 1;
        let nextPos: [number, number] = [0, 0];
        nextPos = [pos[0]+dirs[dirIndex][0], pos[1]+dirs[dirIndex][1]];
        if (checkPosition2(nextPos, boundary_x, boundary_y)) {
            pos = nextPos;
        }
        else {
            // console.log(pos)
            // 改变方向
            dirIndex = (dirIndex + 1) % 4;
            pos[0] += dirs[dirIndex][0]; 
            pos[1] += dirs[dirIndex][1]; 
            if (dirIndex == 0) {
                boundary_y[0] ++;
            }
            else if(dirIndex == 1) {
                boundary_x[0] ++;
            }
            else if(dirIndex == 2) {
                boundary_y[1] --;
            }
            else if(dirIndex == 3){
                boundary_x[1] --;
            }
        }
    }
    return ansMatrix;
};