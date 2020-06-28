class Solution:
    def romanToInt(self, s: str) -> int:
        # roma2ala = {"I": 1, "V", 5, "X", 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        alabo = 0
        for i in range(n-1, -1, -1):
            if s[i] == "I":
                if (i+1) < n and (s[i+1] == "V" or s[i+1] == "X"):
                    alabo -= 1
                else:
                    alabo += 1
            if s[i] == "X":
                if (i+1) < n and (s[i+1] == "L" or s[i+1] == "C"):
                    alabo -= 10
                else:
                    alabo += 10
            if s[i] == "C":
                if (i+1) < n and (s[i+1] == "D" or s[i+1] == "M"):
                    alabo -= 100
                else:
                    alabo += 100
            if s[i] == "V":
                alabo += 5
            if s[i] == "L":
                alabo += 50
            if s[i] == "D":
                alabo += 500
            if s[i] == "M":
                alabo += 1000
        return alabo