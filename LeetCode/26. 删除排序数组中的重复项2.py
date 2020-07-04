class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # l 代表待去重元素的下标
        l = 0
        for i in range(1,n):
            if nums[i] != nums[l]:
                # 找到第一个不重复的数，拷贝到后一位
                nums[l + 1] = nums[i]
                l += 1
        return l + 1