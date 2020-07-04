class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x_reversed = 0
        while x > x_reversed:
            x_reversed = x_reversed * 10 + (x % 10)
            x = int(x / 10)
        return (x == x_reversed) or (x == int(x_reversed / 10))