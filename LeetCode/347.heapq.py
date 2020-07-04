from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)

        for i in nums:
            numsDict[i] += 1
        # print(numsDict)
        heap = []

        for key in numsDict:
            if len(heap) >= k and numsDict[key] < heap[0][1]:
                continue;
            heapq.heappush(heap, (key, numsDict[key]))
            if len(heap) > k:
                heapq.heappop(heap)
            
            # print(heap)


        ans = []
        ans = [x[0] for x in heap]

        return ans