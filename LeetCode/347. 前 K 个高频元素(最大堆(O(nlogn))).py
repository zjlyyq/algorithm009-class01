class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for i in nums:
            if i not in numsMap:
                numsMap[i] = 1
            else:
                numsMap[i] += 1

        numsCount = set()

        for key in numsMap:
            numsCount.add((numsMap[key], key))

        return self.heapQueue(k, numsCount)

    # heap insert
    def heapInsert(self, heap, node):

        heap.append(node)
        heapSize = len(heap)
        cur = heapSize - 1
        pre = (cur - 1) // 2

        while cur > 0 and heap[cur][0] > heap[pre][0]:
            heap[cur], heap[pre] = heap[pre], heap[cur]
            cur = pre
            pre = (cur - 1) // 2

    # heap getTop
    def pollHead(self, heap):

        ret = heap[0]
        heapSize = len(heap)
        heap[0] = heap[heapSize - 1]
        cur = 0

        while (cur*2 + 1) < heapSize - 1:
            left = cur * 2 + 1
            right = cur * 2 + 2
            next = left
            if right > heapSize - 1 or heap[left][0] > heap[right][0]:
                next = left
            else:
                next = right
            if heap[cur][0] < heap[next][0]:
                heap[cur], heap[next] = heap[next], heap[cur]
                cur = next
            else:
                break
            
        heap.pop()
        return ret[1]

    # 从字典中构建最大堆
    def heapQueue(self, k, map):
        heapSize = len(map)
        heap = []
        for i in map:
            self.heapInsert(heap, i)
        ret = []
        for i in range(k):
            ret.append(self.pollHead(heap))
        return ret