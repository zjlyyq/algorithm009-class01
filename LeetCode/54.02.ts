function spiralOrder2(matrix: number[][]): number[] {

    if (!matrix.length || !matrix[0].length) {
        return [];
    }
    let ans2:number[] = [];
    let row_size = matrix.length;
    let col_size = matrix[0].length;
    let boundary_top: number = 0;
    let boundary_bottom: number = row_size - 1;
    let boundary_left: number = 0;
    let boundary_right: number = col_size - 1;
    let count = row_size*col_size;
    while(count > 0){
        for (let i = boundary_left; i <= boundary_right;i ++) {
            ans2.push(matrix[boundary_top][i]);
            count --;
        }
        boundary_top ++;
        for (let i = boundary_top; i <= boundary_bottom;i ++) {
            ans2.push(matrix[i][boundary_right]);
            count --;
        }
        boundary_right --;
        for (let i = boundary_right; i >= boundary_left;i --) {
            ans2.push(matrix[boundary_bottom][i]);
            count --;
        }
        boundary_bottom --;
        for (let i = boundary_bottom; i >= boundary_top;i --) {
            ans2.push(matrix[i][boundary_left]);
            count --;
        }
        boundary_left ++;
    }
    return ans2;
};