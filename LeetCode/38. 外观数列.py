class Solution:
    def countAndSay(self, n: int) -> str:
        last = "1"
        res = "1"
        for i in range(1,n):
            res = self.getSum(last)
            last = res
        
        return res

    
    def getSum(x):
        ret = ""
        n = len(x)
        count = 1
        for i in range(1,n):
            if x[i] == x[i-1]:
                count = count + 1
                if i == n-1:
                    ret = ret + str(count) + x[i-1]
            else:
                ret = ret + str(count) + x[i-1]
                count = 1
                if i == n-1:
                    ret = ret + str(count) + x[i]
            
