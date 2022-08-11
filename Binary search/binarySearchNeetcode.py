from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    l, r  = 0, len(nums) - 1

    while (l <= r):
        mid = (l + r) // 2

        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
    return -1

binarySearch([1,2,4,6,8,9,11,13,15,17,19], 8)
