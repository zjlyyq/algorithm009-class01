class Solution:
    def dailyTemperatures(self, T):
        ans = []
        length = len(T)
        for i in range(length):
            ans.append(0)
        stack = []
        for i in range(length):
            while stack and T[stack[-1]] < T[i]:
                # print(stack[-1])
                # ans[stack[-1]] = i - stack.pop()
                small = stack.pop()
                ans[small] = i - small
            stack.append(i)
        return ans 

l = [73,74,75,71,69,72,76,73]
s = Solution()
print(s.dailyTemperatures(l))