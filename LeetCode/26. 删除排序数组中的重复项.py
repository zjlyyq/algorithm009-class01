class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        l = 0
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                if l == 0:
                    l = i
            else:
                if l != 0:
                    nums[l] = nums[i]
                    l += 1
        if l == 0:
            l = len(nums)
        return l