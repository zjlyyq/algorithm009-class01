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
        flag = True
        while len(queue)  > 0 and flag:
            queueSize = len(queue)
            # 下一层的节点
            nextLevel = []
            for i in range(queueSize):
                cur = queue.pop(0)
                if cur == endWord:
                    # flag = False
                    # print(pathDict[cur])
                    continue
                for j in range(lenOfString):
                    for x in range(26):
                        newStr = cur[:j] + chr(97+x) + cur[j+1:]
                        # print(newStr)
                        if (newStr not in cache or newStr == endWord) and (newStr in wordDict):
                            queue.append(newStr)
                            if newStr not in pathDict: 
                                pathDict[newStr] = set()
                                pathDict[newStr].add(cur)
                            else: pathDict[newStr].add(cur)
                            nextLevel.append(newStr)
            for node in nextLevel:
                queue.append(node)
                cache.add(node)
        print(pathDict)
        if endWord not in pathDict: return []
        self.dfs(pathDict, endWord, beginWord, [], res)
        minlen = 1 << 31
        for i in res:
            if len(i) < minlen: minlen = len(i)
        trueAns = []
        for i in res:
            if len(i) == minlen: trueAns.append(i)
        return trueAns;

    def dfs(self, dict, key, endStr, pathArr, res):
        pathArr.append(key)
        if key == endStr:
            pathArr.reverse()
            res.append(pathArr)
            return
        for i in dict[key]:
            arr = pathArr+[]
            self.dfs(dict, i, endStr, arr, res)



wordList = 