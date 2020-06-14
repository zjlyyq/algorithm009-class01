class Solution:
    leastTimes = -1
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        cache = set()
        wordDict = set(wordList)
        cache.add(beginWord)
        queue = [beginWord]
        # queue.append(beginWord)
        count = 1
        lenOfString = len(beginWord)
        while len(queue) > 0:
            queueSize = len(queue)
            for i in range(queueSize):
                cur = queue.pop(0)
                if cur == endWord: return count;
                for j in range(lenOfString):
                    for x in range(26):
                        newStr = cur[:j] + chr(97+x) + cur[j+1:]
                        if newStr not in cache and newStr in wordDict:
                            queue.append(newStr)
                            cache.add(newStr)

            count  = count + 1
        return 0;
