class Solution:
    leastTimes = -1
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord): return 0;
        wordDict = set(wordList)
        cache = set()
        cache.add(beginWord)
        self.dfs(beginWord, endWord, wordDict, cache, 0, -1)
        return self.leastTimes+1

    def dfs(self, beginWord, endWord, wordDict, cache, times, lasted):
        print(cache)
        if beginWord == endWord:
            if self.leastTimes == -1: self.leastTimes = times
            else: self.leastTimes = min(self.leastTimes, times)
        lenStr = len(beginWord)
        for i in range(lenStr):
            if i == lasted: continue
            for j in range(26):
                newBeginWord = beginWord[:i] + chr(97+j) + beginWord[i+1:]
                if (newBeginWord in wordDict) and (newBeginWord not in cache):
                    print(newBeginWord)
                    cache.add(newBeginWord)
                    self.dfs(newBeginWord, endWord, wordDict, cache, times+1, i)
                    cache.remove(newBeginWord)