def search(nums, target: int) -> int:
  l = 0
  r = len(nums) - 1

  while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      l = mid + 1
    else:
      r = mid - 1

  return -1

nums = [1,2,3,4,5]

actual = search(nums, 3)
print(actual)
