class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                ans[stack.pop()] = i
            stack.append(i)
        while stack:
            ans[stack.pop()] = -1
        
        result = []
        for i in nums1:
            result.append(ans[i])
        return result
            