def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        sum = numbers[left] + numbers[right]
        if sum > target:
            right -= 1

        elif sum < target:
            left += 1

        else:
            return [left + 1, right + 1]

    return [0,0]


