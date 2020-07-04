class Solution:
    ret = False
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        visited = [False] * n
        isPalced= [False] * n
        pathCache = set()

        def set2Int(s):
            base = 1
            ret = 0
            for i in s:
                ret = ret + base * i
                base = base * 2
            return ret

        # 递归求解0-1背包 + 回溯
        # count 求出目标值得次数
        def dfs(path, level, weight, count):
            # print(path)
            if level == n or weight == target:
                # pathCache.add(set2Int(path))
                # print(pathCache)
                if weight == target:
                    # print("path")
                    for i in path:
                        isPalced[i] = True
                    weight = 0
                    count = count + 1
                    path = set()
                if count == k:
                    self.ret = True
            
            for i in range(n):
                if not visited[i] and not isPalced[i] and weight + nums[i] <= target and not self.ret:
                    path.add(i)
                    # print(path)
                    visited[i] = True
                    dfs(set(path), level + 1, weight + nums[i], count)
                    visited[i] = False
                    path.remove(i)
                
        sum_nums = sum(nums)
        target = sum_nums // k
        # print(target)
        if sum_nums % k != 0:
            return False
        cache = [[False]*(target+1) for i in range(n)]
        # print(cache)
        nums.sort()
        print(nums)
        if nums[-1] > target:
            return False
        visited[0] = True
        s = set()
        s.add(0)
        # print(set(s))
        dfs(set(s), 1, nums[0], 0)
        return self.ret
        
        
'''
[730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908]
4
[4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2]
13
'''