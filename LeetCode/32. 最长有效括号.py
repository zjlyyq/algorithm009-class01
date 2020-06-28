'''
思路：以子串的最后下标遍历
dp[i]，以下标i为结尾的最长合法子串的长度
s[i] == '(' ==> dp[i] = 0

s[i],s[i-1] == '()' ==> dp[i] = dp[i-2] + 2
s[i],s[i-1] == '))' ==> dp[i] = if s[i-dp[i-1]] == '(' ,dp[i] = dp[i-1] + 2
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = 0
        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
                continue
            if s[i-1] == ')':
                # "(()))())(" 以这个样例为例，i-dp[i-1]-1 可能会超出范围
                if s[i-dp[i-1]-1] == '(' and (i-dp[i-1]-1) >= 0:
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                else:
                    dp[i] = 0
            if s[i-1] == '(':
                dp[i] = dp[i-2] + 2
        
        return max(dp)