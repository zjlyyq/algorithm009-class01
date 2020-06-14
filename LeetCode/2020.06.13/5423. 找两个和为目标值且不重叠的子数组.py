class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        a_size = len(arr)
        # ans = [a_size + 1]*2
        ans = []
        # 前缀和
        suffix_sum = [0]*(a_size+1)
        # 前缀和位置
        suffix_pos = {}
        suffix_pos[0] = [-1]
        for i in range(a_size):
            cur = i + 1
            suffix_sum[cur] = suffix_sum[i] + arr[i]
            if suffix_sum[cur] not in suffix_pos:
                suffix_pos[suffix_sum[cur]] = [i]
            else:
                suffix_pos[suffix_sum[cur]].append(i)
            if suffix_sum[cur] < target:
                continue
            else:
                if suffix_sum[cur]-target in suffix_pos:
                    for pos in suffix_pos[suffix_sum[cur]-target]:
                        ans.append((i - pos, i, pos))
        print(suffix_sum)
        print(suffix_pos)
        ans.sort()
        print(ans)
        if len(ans) < 2: return -1
        ret = 0
        last = ans[0]
        count = 1
        for i in range(1, len(ans)):
            cur = ans[i]
            print(cur)
            if (cur[1] > last[1] and cur[2] < last[1]) or (last[1] > cur[1] and last[2] < cur[1]):
                continue
            count = count + 1
            ret = ret + cur[0]
            break
        if count < 2: 
            return -1
        else:
            return ret


