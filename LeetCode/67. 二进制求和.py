class Solution:
    def addBinary(self, a: str, b: str) -> str:
        base = 1
        ans = 0
        carry = 0
        len_a = len(a)
        len_b = len(b)
        while len_a > 0 or len_b > 0:
            if len_a > 0:
                carry += int(a[len_a - 1])
                len_a -= 1
            if len_b > 0:
                carry += int(a[len_b - 1])
                len_b -= 1
            ans += (carry % 2) * base
            carry /= 2
            base *= 2
        return ans
        