#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        # 路径缓存-集合类型
        cache = {beginWord}
        # 用于保存路径，最后逆向遍历出原路径
        pathDict = {}
        pathDict[beginWord] = None
        # 路径集合，查找效率比数组高
        wordDict = set(wordList)
        # 队列 优化为直接保存路径
        queue = [[beginWord]]
        lenOfString = len(beginWord)
        flag = True
        while len(queue)  > 0:
            queueSize = len(queue)
            nextLevel = []
            for i in range(queueSize):
                curPath = queue.pop(0)
                cur = curPath[-1]
                if cur == endWord:
                    res.append(curPath)
                    break
                if not flag:
                    break
                for j in range(lenOfString):
                    for x in range(26):
                        newStr = cur[:j] + chr(97+x) + cur[j+1:]
                        if newStr not in cache and newStr in wordDict:
                            newPath = [] + curPath
                            newPath.append(newStr)
                            queue.append(newPath)
                            nextLevel.append(newStr)
            cache.update(nextLevel)
        if not res: return []
        return res
# @lc code=end

