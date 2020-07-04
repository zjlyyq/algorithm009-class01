class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowSize = len(grid)
        colSize = len(grid[0])
        visited = set()
        ans = 0
        for i in range(rowSize):
            for j in range(colSize):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans = ans + 1
                    self.bfs(i, j, grid, visited)
        return ans
                    

    def bfs(self, i, j, grid, visited):
        queue = []
        queue.append((i,j))
        while queue:
            queueSize = len(queue)
            for i in range(queueSize):
                (ii, jj) = queue.pop(0)
                visited.append((ii, jj))
                if grid[ii][jj+1] == "1" and (ii, jj + 1) not in visited:
                    queue.append((ii, jj + 1)) 
                if grid[ii + 1][jj] == "1" and (ii+1, jj) not in visited:
                    queue.append((ii+1, jj)) 

