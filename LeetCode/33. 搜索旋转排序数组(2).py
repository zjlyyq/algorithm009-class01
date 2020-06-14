class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arrSize = len(nums)
        low = 0
        high = arrSize-1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target: return mid
            if nums[mid] < nums[0]:
                if nums[high] < target:
                    high = mid - 1;
                else:
                    if nums[mid] > target:
                        high = mid -1
                    else:
                        low = mid + 1
            if nums[mid] >= nums[0]:
                if nums[0] > target:
                    low = mid + 1
                else:
                    if nums[mid] > target:
                        high = mid -1
                    else:
                        low = mid + 1
        return -1