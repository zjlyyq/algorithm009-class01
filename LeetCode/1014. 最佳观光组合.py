class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        preMax = 0
        ans = 0
        a_size = len(A)
        for i in range(a_size):
            if A[i] - i + preMax > ans:
                ans = A[i] - i + preMax        
        if A[i] + i > preMax:
            preMax = A[i] + i
        return ans