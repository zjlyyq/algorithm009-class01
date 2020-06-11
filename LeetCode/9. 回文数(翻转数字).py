class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x_reversed = 0
        x_length = 0
        x_copy = x
        while x_copy > 0:
            x_copy = int(x_copy / 10)
            x_length = x_length + 1
        l = int(x_length / 2)
        while l > 0:
            x_reversed = x_reversed * 10 + (x % 10)
            x = int(x / 10)
            l = l - 1
        if (x_length % 2) != 0: 
            x = int(x / 10)
        return x == x_reversed
