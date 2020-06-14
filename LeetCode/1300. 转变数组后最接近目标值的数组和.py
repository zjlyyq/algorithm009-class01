class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        sum = 0
        maxNum = -1
        maxCount = 0
        for i in arr:
            if i > maxNum:
                maxCount = 1
                maxNum = i
            sum += i
        dir = 0
        if sum > target:
            offset = sum - target
            dir = -1
        else: 
            offset = target - sum
            dir = 1

        offset = int(offset / maxCount)
        offset2 = offset + dir
        if abs(sum + dir*offset - target) > abs(sum + dir*offset2 - target):
            return maxNum + dir*offset
        else:  
            return maxNum + dir*offset2
        
        