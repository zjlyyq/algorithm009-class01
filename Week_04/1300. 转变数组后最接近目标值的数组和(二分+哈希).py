class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        def binary_search_fitst(target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] > target: right = mid - 1
                else: left = mid + 1
            return left
        def getChange(sum, value):
            sum_cp = sum
            s = binary_search_fitst(value)
            for i in range(s,len(arr)):
                sum_cp = sum_cp - (arr[i]-value)
            return sum_cp
        
        left, right = 0, max(arr)
        ans = 0
        sum = 0
        offset = 1 << 31
        for i in arr: sum = sum + i
        while left <= right:
            mid = (left+right) // 2
            sum_cp = getChange(sum,mid)
            if sum_cp < target:
                left = mid + 1
                if target - sum_cp < offset:
                    offset = target - sum_cp
                    value = mid
                if target - sum_cp == offset:
                    if mid < value:
                        value = mid
            else:
                right = mid - 1
                if sum_cp - target < offset:
                    offset = sum_cp - target
                    value = mid
                if sum_cp - target == offset:
                    if mid < value:
                        value = mid
        return value