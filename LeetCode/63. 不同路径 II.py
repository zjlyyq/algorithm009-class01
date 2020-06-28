class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n= len(obstacleGrid[0]), len(obstacleGrid)

        dp = [[0] * m for _ in range(n)] 
        for i in range(n):
            if obstacleGrid[i][m-1] == 0:
                dp[i][m-1] = 1
        for i in range(m):
            if obstacleGrid[n-1][i] == 0:
                dp[n-1][i] = 1
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                else:
                    dp[i][j] = 0
        return dp[0][0]