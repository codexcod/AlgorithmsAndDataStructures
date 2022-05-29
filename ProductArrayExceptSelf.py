def productOfArrayExceptSelf(arr):
    leftProducts = [1] * len(arr)
    rightProducts = [1] * len(arr)
    result = [1] * len(arr)

    leftProducts[0] = 1
    rightProducts[len(arr) - 1] = 1

    for i in range(1,len(arr)):
        leftProducts[i] = arr[i - 1] * leftProducts[i - 1]

    for i in range(len(arr) - 2,-1,-1):
        rightProducts[i] = arr[i + 1] * rightProducts[i + 1]

    for i in range(len(arr)):
        result[i] = rightProducts[i] * leftProducts[i]

    return result


def productOfArrayExceptSelfNoMemory(arr):
    result = [1] * len(arr)

    result[0] = 1
    for i in range(1,len(arr)):
        result[i] = arr[i - 1] * result[i - 1]

    rightNumbers = 1
    for i in range(len(arr) - 1,-1,-1):
        result[i] = rightNumbers * result[i]
        rightNumbers *= arr[i]

    return result


print(productOfArrayExceptSelfNoMemory([1,2,3,4]))
