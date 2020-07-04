class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numsc = nums + nums[:-1]
        ans = [0]*len(numsc)
        stack = []
        for i in range(len(numsc)):
            while stack and numsc[stack[-1]] < numsc[i]:
                ans[stack.pop()] = numsc[i]
            stack.append(i)
        while stack:
            ans[stack.pop()] = -1
            
        return ans[:len(nums)]