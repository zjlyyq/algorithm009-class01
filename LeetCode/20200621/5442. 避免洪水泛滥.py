from collections import deque
from collections import defaultdict
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dq = deque()
        pools = defaultdict(int)
        for x in rains:
            if x > 0:
                dq.append(x)
                pools[x] = 0
        ans = []
        for i in range(len(rains)):
            if rains[i] > 0:
                if pools[rains[i]] == -1:
                    return []
                pools[rains[i]] = -1
                ans.append(-1)
                dq.popleft()
            else:
                for j in range(len(dq)):
                    if dq[j] in pools and pools[dq[j]] == -1:
                        ans.append(dq[j])
                        pools[dq[j]] = 0
                        break
                if len(ans) < (i+1):    
                    ans.append(1)
        return ans
