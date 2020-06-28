class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        d = set()
        for i in range(0,n-3):
            for j in range(i+1, n-2):
                k, q = j + 1, n-1
                s = target - nums[i] - nums[j]
                while k < q:
                    if nums[k] + nums[q] < s:
                        k += 1
                    elif nums[k] + nums[q] > s:
                        q -= 1
                    else:
                        l = [nums[i], nums[j], nums[k], nums[q]]
                        k += 1
                        if str(l) not in d:
                            ans.append(l)
                            d.add(str(l))
        return ans
                    