class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # d['a']表示字符a上次出现的坐标
        d = {}
        n = len(s)
        ans = 0
        l, r = 0, 0
        while r < n:
            cur = s[r]
            if cur in d and d[cur] >= l:
                l = d[cur] + 1
            else:
                if (r - l + 1) > ans:
                    ans = r-l+1
            d[cur] = r
            r += 1
        return ans