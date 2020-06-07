class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if (n == 1):
             return ["()"]
        if (n == 0):
            return []
        s = set()
        l1 = []
        l2 = []
        for j in range(n):
            l1 = self.generateParenthesis(j)
            l2 = self.generateParenthesis(n-j-1)
            if l2:
                if l1:
                    for str1 in l1:
                        for str2 in l2:
                            s.add("("+str1+")" + str2)
                else:
                    for str2 in l2:
                        s.add("("+")" + str2)
            else:
                for str1 in l1:
                    s.add("("+str1+")")

        l = list(s)
        l.sort()
        return l