import math
from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)

    while (left + 1 < right):
        mid = math.ceil((right + left) / 2)  # This is where I found the error, where Sambol did floor division (//) instead of float division (/)
        # mid = (right + left) // 2 # this is what Sambol accidentally did where his code rounded down instead of up like his explanation
        print(f'Mid value is: {nums[mid]}')
        
        if (target == nums[mid]):
            print(f'Found target element: {nums[mid]}')
            return nums[mid]
        elif (target < nums[mid]):
            print(f'Target value {target} is less than current middle value: {nums[mid]}')
            right = mid
            print(f'Right index has moved to: {right}')
        else:
            print(f'Target value {target} is greater than current middle value: {nums[mid]}')
            left = mid
            print(f'Left index has moved to: {left}')
        print("Iteration completed")

    if (nums[left] == target):
        return nums[left]
    return -1

binarySearch([1,2,4,6,8,9,11,13,15,17,19], 8)
