class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        bmDayPos = {}
        for i in range(len(bloomDay)):
            if i not in bmDayPos:
                bmDayPos[bloomDay[i]] = [i + 1]
            else:
                bmDayPos[i].append(i + 1)
        bmDayPos = {k: v for k, v in sorted(bmDayPos.items(), key=lambda item: item[1])}
        print(bmDayPos)
        ret = 0
        ans = []
        for key in bmDayPos:
            ret = key
            ans = ans +bmDayPos[key]
            print(ans)
            print(self.check(ans, m, k))
            if self.check(ans, m, k):
                return ret
        return -1
    def check(self, arr, m, k):
        if len(arr) < m*k: return False
        if k == 1: 
            return True
        last = 0
        count = 0
        while last < len(arr):
            flag = False
            for i in range(1,k):
                if i+last >= len(arr) or arr[i+last] - arr[last] > 1:
                    flag = True
                    last = i+last
                    break
            if flag:
                count = count + 1
            else:
                last = last + 1
        return count >= m