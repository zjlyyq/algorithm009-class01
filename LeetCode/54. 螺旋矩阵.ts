function spiralOrder(matrix: number[][]): number[] {
    // chaek the position 
    function checkPosition(pos: [number, number], boundary_x: [number, number], boundary_y: [number, number]): boolean {
        if (pos[0] == boundary_x[1] || pos[0] == boundary_x[0]) {
            return false;
        }
        if (pos[1] == boundary_y[1] || pos[1] == boundary_y[0]) {
            return false;
        }
        return true;
    }

    if (!matrix.length || !matrix[0].length) {
        return [];
    }
    // 按顺时针定义方向
    let dirs: [number,number][] = [ [0 ,1], [1, 0], [0, -1], [-1, 0] ];
    // 起始位置
    let pos: [number, number] = [0, 0]
    // 起始方向
    let dirIndex:number = 0;
    let row_size = matrix.length;
    let col_size = matrix[0].length;
    let boundary_x: [number, number] = [-1,row_size];
    let boundary_y: [number, number] = [-1,col_size];
    let ans: number [] = [];
    for(let i = 0;i < row_size*col_size;i ++) {
        ans.push(matrix[pos[0]][pos[1]])
        let nextPos: [number, number] = [0, 0];
        nextPos = [pos[0]+dirs[dirIndex][0], pos[1]+dirs[dirIndex][1]];
        if (checkPosition(nextPos, boundary_x, boundary_y)) {
            pos = nextPos;
        }
        else {
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
    return ans;
};