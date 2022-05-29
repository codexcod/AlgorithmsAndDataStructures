def search(nums,target):
    left = 0
    right = len(nums) - 1
    #We use binary search here to look whee the sorted array is broken
    while left < right:
        midPoint = left + (right - left) // 2
        if nums[midPoint] > nums[right]:
            left = midPoint + 1

        else:
            right = midPoint

    start = left
    left = 0
    right = len(nums) - 1

    #Then we se in wich part of the array the target is by compraing ti with the numbers we had before
    if target >= nums[start] and target <= nums[right]:
        left = start

    else:
        right = start

    #Finally we do another binary search to find the target
    while left <= right:
        midPoint = left + (right - left) // 2
        if nums[midPoint] == target:
            return midPoint

        elif nums[midPoint] < target:
            left = midPoint + 1

        else:
            right = midPoint - 1

    return -1


print(search([4,5,6,7,8,-1,0,1,2,3],2))