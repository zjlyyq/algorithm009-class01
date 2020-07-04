class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        a = 0
        for i in range(n):
            a = start + 2 * i
            ans ^= a
        return ans