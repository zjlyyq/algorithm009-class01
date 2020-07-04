'''
度数都是0一样的情况下，优先上出度小的
'''
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        indeed = []
        # 入边
        inedges = [[] for _ in range(n+1)]
        # 出边
        outedges = [[] for _ in range(n+1)]
        
        for edge in dependencies:
            iin = edge[1]
            out = edge[0]
            inedges[iin].append(out)
            outedges[out].append(iin)

        queue = []
        for i in range(1,n+1):
            if len(inedges[i]) == 0:
                queue.append(i)
            
        ans = 16
        
        def dfs(queue, k, day):
            if not queue:
                if ans > day:
                    ans = day
            return
        
            if qsize <= k:
                for i in range(qsize):
                    c = queue.pop(0)
                    for inn in outedges[c]:
                        inedges[inn].remove(c)
                        if len(inedges[inn]) == 0:
                            queue.append(inn)
                    outedges[c] = []
                print(queue)
                dfs(queue, in)
            else:
                for i in range(k):
                    c = queue.pop(0)
                    for inn in outedges[c]:
                        inedges[inn].remove(c)
                        if len(inedges[inn]) == 0:
                            queue.append(inn)
                    outedges[c] = []
                print(queue)
        dfs(queue, k, 0)
        return ans
        print(queue)
        while k > 0 and queue:
            qsize = len(queue)
            ans += 1
            if qsize <= k:
                for i in range(qsize):
                    c = queue.pop(0)
                    for inn in outedges[c]:
                        inedges[inn].remove(c)
                        if len(inedges[inn]) == 0:
                            queue.append(inn)
                    outedges[c] = []
                print(queue)
            else:
                # 优先输出出度最多的节点
                q.sort()
                for i in range(k):
                    c = queue.pop(0)
                    for inn in outedges[c]:
                        inedges[inn].remove(c)
                        if len(inedges[inn]) == 0:
                            queue.append(inn)
                    outedges[c] = []
                print(queue)
        return ans
        