class Solution:
    ans = False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 保存前缀被匹配上的下标
        l = []
        for i in range(len(s)):
            for pos in l:
                if s[pos+1: i+1] in wordDict:
                    l.append(i)
        
        return l[-1] == len(s) - 1