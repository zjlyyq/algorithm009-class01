class Solution:
    ret = False
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def search(groups):
            if not nums: return True
            num = nums.pop()
            for i, group in enumerate(groups):
                if group + num <= target:
                    groups[i] += num
                    if search(groups): return True
                    groups[i] -= num
                if not group:
                    break

            # 回溯部分
            nums.append(num)
            return False

        target, mod = divmod(sum(nums), k)
        # print(target)
        if mod:
            return False
        # 关键一步
        nums.sort()
        print(nums)
        return search([0]*k)
        
        