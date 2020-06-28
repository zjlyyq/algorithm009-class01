class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = [[] for i in range(numRows)]
        downdir = True
        rowindex = 0
        i = 0
        while i < len(s):
            for j in range(numRows):
                l[j].append(s[i])
                i += 1
            for j in range(numRows-2, -1, -1):
                l[j].append(s[i])
                i += 1
        ans = ""
        for i in l:
            for j in i:
                ans += j
        return ans