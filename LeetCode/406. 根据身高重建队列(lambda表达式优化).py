class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        print(people)
        ans = []
        for i in people:
            ans.insert(i[1], i)
        return ans