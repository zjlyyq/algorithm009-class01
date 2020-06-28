class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        # print(nums)

        i, j = 0, len(nums)

        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] == target:
                return [i, j]
            else:
                j -= 1