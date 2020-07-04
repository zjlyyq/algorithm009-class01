class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeropos = 0
        notzeropos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[zeropos], nums[i] = nums[i], nums[zeropos]
                zeropos += 1

        print(nums)