class Solution:
    def totalNQueens(self, n: int) -> int:
        positions = [0]*n
        ret = [0]
        # positons:皇后的位置数组
        def isOk(positions, n):
            sum1 = {positions[0]}
            sum2 = {0-positions[0]}
            cols = {positions[0]}
            for i in range(1, n):
                hang_x, hang_y = i + positions[i], i - positions[i]
                if positions[i] in cols or hang_x in sum1 or hang_y in sum2:
                    return False
                cols.add(positions[i])
                sum1.add(hang_x)
                sum2.add(hang_y)
            return True

        # 回溯找路径
        def backTrack(r_index, n, positions):
            if r_index == n:
                if isOk(positions, n):
                    ret[0] = ret[0] + 1
                return
            for i in range(n):
                positions[r_index] = i
                if isOk(positions, r_index + 1):
                    backTrack(r_index+1, n, positions)

        backTrack(0, n, positions)
        return ret[0]
