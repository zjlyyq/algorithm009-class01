class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        while g and s:
            if s[0] >= g[0]: 
                count = count + 1
                s.pop(0)
                g.pop(0)
            else:
                s.pop(0)
        return count