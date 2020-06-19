from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = defaultdict(int)

        for i in nums:
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

        while cur > 0 and node[0] > heap[pre][0]:
            heap[cur] = heap[pre]
            cur = pre
            pre = (cur - 1) // 2

        heap[cur] = node

    
    def pollHead2(self, heap):
        ret = heap[0]
        heapSize = len(heap)
        heap[0] = heap[heapSize - 1]
        pos = 0
        childpos = 2*pos + 1 
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
    # heap getTop
    def pollHead(self, heap):
        ret = heap[0]
        if len(heap) == 1:
            return heap.pop()[1]
        heap[0] = heap.pop()
        newItem = heap[0]
        endpos = len(heap)
        pos = 0
        childpos = pos * 2 + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and heap[childpos][0] < heap[rightpos][0]:
                childpos = rightpos
            if heap[pos][0] < heap[childpos][0]:
                heap[pos], heap[childpos] = heap[childpos], heap[pos]
                pos = childpos
                childpos = 2 * pos + 1 
            else:
                break;       
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