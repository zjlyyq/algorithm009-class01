class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        positions = [0]*n

        # 打印答案
        def printQueue(positions, n):
            strings = []
            for i in positions:
                s = ""
                for j in range(n):
                    if j == i:
                        s += "Q"
                    else:
                        s += "."
                strings.append(s)
            ans.append(strings)
        
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
                    printQueue(positions, n)
                return
            for i in range(n):
                positions[r_index] = i
                if isOk(positions, r_index + 1):
                    backTrack(r_index+1, n, positions) 

        backTrack(0, n, positions)
        return ans