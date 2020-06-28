from collections import deque
from collections import defaultdict
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 记录晴天下标，自然递增，二分
        sundays = []
        n = len(rains)
        ans = [-2] * n
        fullpoll = defaultdict(int)
        for i in range(n):
            poll = rains[i]
            lastrainyday = fullpoll[poll]
            if poll == 0:
                sundays.append(i+1)
                continue;
            # 湖泊已经满了
            if lastrainyday > 0:
                if sundays:
                    # 二分查找第一个大于上次下雨的日期
                    l, r = 0, len(sundays)-1
                    while l <= r:
                        mid = l + (r-l) // 2
                        if sundays[mid] > lastrainyday:
                            r = mid - 1
                        else:
                            l = mid + 1
                    # 找不到大于上次下雨的晴天，返回【】
                    if r == len(sundays)-1:
                        return []
                    else:
                        #  第一个晴天抽干该湖泊
                        ans[sundays[r+1]-1] = poll
                        ans[i] = -1
                        fullpoll[poll] = i+1
                        # 删除该晴天
                        sundays.pop(r+1)
                else:
                    return []
            # 湖泊为空
            else:
                fullpoll[poll] = i + 1
                ans[i] = -1
        for i in range(len(ans)):
            if ans[i] == -2:
                ans[i] = 1
        return ans