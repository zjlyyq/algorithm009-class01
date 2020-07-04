class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arrSize = len(nums)
        # 计算出数组起点的偏移量offset,也就是所有元素的偏移量offset
        offset = self.getTurnPoint(nums)
        low = 0
        high = arrSize-1
        while low <= high:
            mid = int((low + high) / 2)
            # 数组进过翻转后已经产生了偏移，实际位置是(mid+offset)%arrSize
            if nums[(mid+offset)%arrSize] == target: return (mid+offset)%arrSize
            elif nums[(mid+offset)%arrSize] < target: low = mid + 1
            else: high = mid - 1
        return -1

    def getTurnPoint(self, nums: List[int]) -> int:
        arrSize = len(nums)
        for i in range(arrSize):
            if nums[i] <= nums[(i-1)%arrSize]: 
                return i
    