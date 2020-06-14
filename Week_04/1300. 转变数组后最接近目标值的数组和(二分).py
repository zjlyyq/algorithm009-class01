class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        sum = 0
        left, right = 0, max(arr)
        ans = 0
        offset = 1 << 31
        while left <= right:
            mid = (left+right) // 2
            sum_cp = getChange(arr, value)
            if sum_cp < target:
                left = mid + 1
                if target - sum_cp < offset:
                    offset = target - sum_cp
                    value = mid
            else:
                right = mid - 1
                if sum_cp - target < offset:
                    offset = sum_cp - target
                    value = mid

        def getChange(arr, value):
            sum_cp = sum
            for i in arr:
                if i > value:
                    sum_cp = sum_cp - (i-value)
            return sum_cp