class Solution:
    ans = -1
    visited = set()
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set()
        for i in bank:
            bank_set.add(i)
        self.dfs(start, end, 0, bank_set)
        return self.ans

    def dfs(self, start: str, end: str, times: int, bank: set):
        # print(start)
        if start == end: 
            if self.ans == -1: self.ans = times
            else: self.ans = min(self.ans, times)
            return
        chars = ["A", "C", "G", "T"];
        for i in range(8):
            for c in chars:
                if c == start[i]: continue
                newStart = start[:i] + c + start[i+1:]
                if newStart in bank and newStart not in self.visited:
                    self.visited.add(newStart)
                    self.dfs(newStart, end, times + 1, bank)
                    self.visited.remove(newStart)