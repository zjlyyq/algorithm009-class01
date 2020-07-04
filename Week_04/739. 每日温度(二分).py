class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # cache[x]: 大于x的下标数组，之后就是在该数组中二分找第一个大于x元素下标的数
        cache = {}
        for i in range(30,101):
            cache[i] = []
        for i in range(len(T)):
            for j in range(30,T[i]):
                cache[j].append(i)
        ret = []
        for i in range(len(T)):
            rrt = self.binary_search(cache[T[i]], i)
            ret.append(rrt)
        return ret

    # 第一个大于目标值的数 
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        if high == -1 or target > arr[high]: return 0
        if high > 0 and target < arr[low]: return arr[0]-target
        while low <= high:
            mid = low + int((high-low) >> 1)
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return arr[low] - target

