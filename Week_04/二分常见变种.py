def binary_search_fitst_bigger(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left+right) // 2
    if arr[mid] > target: 
      right = mid - 1
    else: 
      left = mid + 1
  # 上述过程保证了在 left <= right的范围内，right的最终位置肯定是满足arr[right] < target的，
  # 循环的终止条件出left所在的位置不越界就是需要的值，否则返回 -1
#   return left if left < len(arr) else -1
  return right+1 if right < len(arr) - 1 else -1



def binary_search_lastest_smaller(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left+right) // 2
    if arr[mid] < target: 
        left = mid + 1
    else: 
        right = mid - 1
  return left - 1

arr = [1,2,3,4,5,6,7,8]
print(binary_search_fitst_bigger(arr, 0))
print(binary_search_lastest_smaller(arr, 0))
