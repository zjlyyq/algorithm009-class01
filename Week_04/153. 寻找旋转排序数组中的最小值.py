class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while(lo <= hi):
            mid = int((lo + hi) / 2)
            if nums[mid] <= nums[0] and mid != 0: 
                hi = mid - 1
            else: 
                lo = mid + 1
        if hi == len(nums)-1:
            return nums[0]
        return nums[hi+1]