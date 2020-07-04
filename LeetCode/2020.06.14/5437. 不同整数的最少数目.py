class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n_count = {}
        for i in arr:
            if i not in n_count:
                n_count[i] = 1
            else:
                n_count[i] = n_count[i] + 1
        n_count_sorted = {k: v for k, v in sorted(n_count.items(), key=lambda item: item[1])}
        ans = 0
        for key in n_count_sorted:
            if n_count_sorted[key] <= k:
                k = k - n_count_sorted[key] 
                continue
            ans  = ans + 1
        return ans