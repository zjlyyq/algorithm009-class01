class Solution:
    leastTimes = -1
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        cache = set()
        pathDict = {}
        wordDict = set(wordList)
        cache.add(beginWord)
        queue = []
        queue.append(beginWord)
        pathDict[beginWord] = None
        count = 1
        lenOfString = len(beginWord)
        while len(queue) > 0:
            queueSize = len(queue)
            print(queueSize)
            for i in range(queueSize):
                cur = queue.pop(0)
                print('cur:' + cur)
                if cur == endWord: 
                    t = endWord
                    while t != None:
                        print(t)
                        print('--->')
                        t = pathDict[t]
                    return count;
                for j in range(lenOfString):
                    for x in range(26):
                        newStr = cur[:j] + chr(97+x) + cur[j+1:]
                        if newStr not in cache and newStr in wordDict:
                            queue.append(newStr)
                            pathDict[newStr] = beginWord
                            cache.add(newStr)
                            # print(newStr == endWord)
            count  = count + 1
        return 0;
