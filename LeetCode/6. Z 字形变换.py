class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = [[] for i in range(numRows)]
        downdir = True
        rowindex = 0
        for i in range(len(s)):
            l[rowindex].append(s[i])
            if downdir and rowindex < (numRows-1):
                rowindex += 1
                continue
            if downdir and rowindex == (numRows-1):
                downdir = not downdir
                rowindex -= 1 
                continue
            if not downdir and rowindex > 0:
                rowindex -= 1
                continue
            if not downdir and rowindex == 0:
                downdir = not downdir
                rowindex += 1
        ans = ""
        for i in l:
            for j in i:
                ans += j
        return ans