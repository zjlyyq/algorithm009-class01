class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            count = 0
            n = len(flowers)
            flowers = [True if v <= day else False for v in bloomDay]
            s,t = 0, 0
            while t < len(flowers):
                if not flowers[t]:
                    count = count + (t - s) // k
                    s = t + 1
                t = t + 1
            count = count + (t - s) // k
            return count >= m

        lo, hi = min(bloomDay), max(bloomDay)
        while lo <= hi:
            mid = (lo+hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo if check(lo) else -1