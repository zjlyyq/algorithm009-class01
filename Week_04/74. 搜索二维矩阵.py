class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            arr.append(row[0])
        r_index = self.binary_search_lastSmall(arr, target)
        return self.binary_search(matrix[r_index], target)
        
    def binary_search_lastSmall(self, arr, target):
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = int((lo + hi) / 2)
            if arr[mid] >= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1
    def binary_search(self, arr, target):
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = int((lo + hi) / 2)
            if arr[mid] == target:
                return true
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
