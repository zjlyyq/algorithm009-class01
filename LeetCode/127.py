class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
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
                    t_list = []
                    while t != None:
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
