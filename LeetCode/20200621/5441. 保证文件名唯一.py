from collections import defaultdict
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        filecounts = defaultdict(int)
        for i in range(len(names)):
            if filecounts[names[i]] > 0:
                c = filecounts[names[i]]
                filecounts[names[i]] += 1
                newname = names[i] + "(" + str(c) + ")"
                while filecounts[newname] > 0:
                    c += 1
                    newname = names[i] + "(" + str(c) + ")"
                names[i] = newname
                filecounts[newname] += 1
            else:
                filecounts[names[i]] += 1
        return names
            