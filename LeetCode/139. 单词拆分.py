class Solution:
    ans = False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(pos, s):
            # print(pos)
            if pos == len(s):
                self.ans = True
                return
            
            word = ''
            for i in range(len(s)-1, pos-1, -1):
                if s[pos:i+1] in wordDict:
                    dfs(i+1, s)
                    if self.ans:
                        return
        
        dfs(0, s)

        return self.ans