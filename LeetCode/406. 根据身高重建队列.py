class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        people.reverse()
        # 保存某个高度的人的数目
        h_count = {}
        reversed_people = people
        for i in reversed_people:
            h = i[0]
            if h not in h_count:
                h_count[h] = 1
            else:
                h_count[h] = h_count[h] + 1
        n = len(reversed_people)
        ans = []
        for i in range(0, n):
            cur = reversed_people[i]
            # 计算这个人应该排在队伍中的位置，已经在队的都是高度大于等于自己的
            index = cur[1] - h_count[cur[0]] + 1           
            ans = ans[0:index] + [cur] + ans[index:]
            # 排好一位，该高度未排队人数计数减一
            h_count[cur[0]] = h_count[cur[0]] - 1
        return ans