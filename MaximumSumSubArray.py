def maximumSumSubarray(arr):
    maxSum = arr[0]
    currentSum = maxSum
    for num in arr:
        currentSum = max(num + currentSum, num)
        maxSum = max(currentSum, maxSum)
        #print("current : ", currentSum , " max : ", maxSum)

    return maxSum



