def sortedSquaredArraySlow(nums):
    # This for loop takes linear time
    for i in range(len(nums)):
        nums[i] **= 2

    # The sort method is always a slow solution as it takes O(N * log(N))
    # This makes the solution slower
    nums.sort()
    return nums


def sortedSquaredArray(nums):
    result = [0] * len(nums)

    left = 0
    right = len(nums) - 1

    # In this case we do it in linear time
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1

        else:
            result[i] = nums[right] ** 2
            right -= 1

    return result


print(sortedSquaredArray([-7, -3, -1, 4, 8, 12]))
