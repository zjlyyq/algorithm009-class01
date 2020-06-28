'''
动态规划：
具有最优子结构

状态表示：dp[i][j] —— 以下标i为结尾长度为j的子串是否为回文串

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*(n+1) for _ in range(n)]
        ans = 0
        for i in range(n):
            dp[i][1] = True
            dp[i][0] = True
            ans += 1
            for j in range(2, i+2):
                if dp[i-1][j-2] == True and s[i] == s[i-j+1]:
                    dp[i][j] = True
                    ans += 1
        return ans