class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = dict()

        for i in nums:
            if i not in numsMap:
                numsMap[i] = 1
            else:
                numsMap[i] += 1
            # numsMap[i] += 1

        numsCount = set()

        for key in numsMap:
            numsCount.add((numsMap[key], key))

        return self.heapQueue(k, numsCount)

    # heap insert
    def heapInsert(self, heap, node, k):
        # 比最小堆顶部元素小，直接丢弃
        if len(heap) >= k and heap[0][0] > node[0]:
            return;
        heap.append(node)
        heapSize = len(heap)
        cur = heapSize - 1
        pre = (cur - 1) // 2

        while cur > 0 and heap[cur][0] < heap[pre][0]:
            heap[cur], heap[pre] = heap[pre], heap[cur]
            cur = pre
            pre = (cur - 1) // 2
        

    # heap getTop
    def pollHead(self, heap):
        heapSize = len(heap)
        heap[0] = heap[heapSize - 1]
        cur = 0

        while (cur*2 + 1) < heapSize - 1:
            left = cur * 2 + 1
            right = cur * 2 + 2
            next = left
            if right > heapSize - 1 or heap[left][0] < heap[right][0]:
                next = left
            else:
                next = right
            if heap[cur][0] > heap[next][0]:
                heap[cur], heap[next] = heap[next], heap[cur]
                cur = next
            else:
                break
            
        heap.pop()

    # 从字典中构建最大堆
    def heapQueue(self, k, map):
        heap = []
        for i in map:
            self.heapInsert(heap, i, k)
            if len(heap) > k:
                self.pollHead(heap)
        ret = []
        ret = [x[1] for x in heap]
        return ret