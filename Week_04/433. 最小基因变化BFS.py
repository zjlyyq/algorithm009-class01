class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        cache = set(start)
        count = 0
        chars = ["A", "C", "G", "T"]
        queue = [start]
        while queue:
            count  = count + 1
            queueSize = len(queue)
            for i in range(queueSize):
                cur = queue.pop(0)
                if cur == end:
                    return count
                for j in range(8):
                    for c in chars:
                        newStart = start[:j] + c + start[j+1:]
                        if newStart in bank_set and newStart not in cache:
                            cache.add(newStart)
                            queue.append(newStart)