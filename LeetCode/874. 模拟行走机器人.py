class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        # 方向下标
        d_index = 0
        ans = 0
        x_cache = {}
        y_cache = {}
        for e in obstacles:
            x = e[0]
            y = e[1]
            if x not in x_cache:
                x_cache[x] = [y]
            else:
                x_cache[x].append(y)
            if y not in y_cache:
                y_cache[y] = [x]
            else:
                y_cache[y].append(x)
        cur = (0,0)
        for i in commands:
            if i == -1:
                d_index = (d_index + 1) % 4
                continue
            elif i == -2:
                d_index = (d_index - 1) % 4
                continue
            move = dirs[d_index]
            next = (cur[0]+move[0]*i,cur[1]+move[1]*i)
            # y方向
            if (d_index == 0 or d_index == 2) and (cur[0] in x_cache) :
                # 用标记记录是否被阻挡过
                flag = False
                for j in x_cache[cur[0]]:
                    if (j-cur[1])*move[1] > 0 and (j-cur[1])*move[1] <= (next[1]-cur[1])*move[1]:
                        next = (next[0],j)
                        flag = True
                if flag:
                    next = (next[0],next[1]-move[1])
            # x方向
            if (d_index == 1 or d_index == 3) and (cur[1] in y_cache):
                # 用标记记录是否被阻挡过
                flag = False
                for j in y_cache[cur[1]]:
                    if (j-cur[0])*move[0] > 0 and (j-cur[0])*move[0] <= (next[0]-cur[0])*move[0]:
                        next = (j, next[1])
                        flag = True
                if flag:
                    next = (next[0]-move[0], next[1])
            ans = max(ans, next[0]*next[0] + next[1]*next[1])
            cur = next
        return ans