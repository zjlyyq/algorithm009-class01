#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution:
    res = []
    min_times = 1 << 31
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def dfs(cur_str, end_str, visited, path_list, times):
            visited.add(cur_str)
            path_list.append(cur_str)
            if cur_str == end_str and times == self.min_times:
                self.res.append([] + path_list)
            if cur_str == end_str and times < self.min_times:
                self.min_times = times
                self.res = []
                self.res.append([] + path_list)
            len_str = len(beginWord)
            for i in range(len_str):
                for j in range(26):
                    new_str = cur_str[:i] + chr(97+j) + cur_str[i+1:]
                    if new_str in wordList and new_str not in visited and new_str != cur_str and times+1 <= self.min_times:
                        dfs(new_str, end_str, visited, path_list, times + 1)
                        path_list.remove(new_str)
                        visited.remove(new_str)
        visited = set()
        dfs(beginWord, endWord, visited, [], 0)
        return self.res
# @lc code=end

