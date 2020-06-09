class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxpos = set()
        maxS = 0;
        ans = []
        for i in range(len(candies)):
            if (candies[i] >= maxS):
                if candies == maxS:
                    maxpos.add(i)
                else:
                    maxpos = [i]
                max = candies[i]
        for i in range(len(candies)):
            if i in maxpos:
                ans.append(true)
            else:
                ans.append(candies[i] + extraCandies > maxS)
            
            