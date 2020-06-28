from collections import defaultdict
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = defaultdict(deque)
        n = len(s)
        for i in range(n):
            dict[s[i]].append(i)
        ans = 0
        l, r = 0, 0
        while r < n:
            cur = s[r]
            while dict[cur][0] < l:
                dict[cur].popleft()
            if dict[cur][0] < r:
                l = dict[cur].popleft() + 1
            else:
                if r - l + 1 > ans:
                    ans = r - l + 1
            r += 1
        return ans