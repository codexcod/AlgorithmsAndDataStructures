def findStartingIndex(nums, target):
    index = -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        midpoint = start + (end - start) // 2
        if nums[midpoint] >= target:
            end = midpoint - 1

        else:
            start = midpoint + 1

        if nums[midpoint] == target:
            index = midpoint

    return index


def findEndingIndex(nums, target):
    index = -1

    start = 0
    end = len(nums) - 1


    while start <= end:
        midpoint = start + (end - start) // 2
        if nums[midpoint] <= target:
            start = midpoint + 1

        else:
            end = midpoint - 1

        if nums[midpoint] == target:
            index = midpoint

    return index


def searchRange(nums, target):
    result = [-1, -1]
    result[0] = findStartingIndex(nums, target)
    result[1] = findEndingIndex(nums, target)
    return result

arr = [1,1,2,2,2,3,3,3,4,4,4,5,5,5]
print(searchRange(arr,3))