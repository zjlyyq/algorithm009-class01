class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = ans = minSum = nums[0]
        for i in range(1,len(nums)):
            sum = sum + nums[i]
            ans = sum - minSum
            if sum < minSum: minSum = sum
        
        return ans


            