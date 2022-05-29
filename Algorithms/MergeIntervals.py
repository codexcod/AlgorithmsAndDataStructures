def mergeIntervals(array):
    if len(array) <= 1:
        return array

    result = []
    currentInterval = array[0]
    result.append(currentInterval)
    for interval in array:
        currentEnd = currentInterval[1]
        nextBegin = interval[0]
        nextEnd = interval[1]

        if currentEnd >= nextBegin:
            currentInterval[1] = max(currentEnd, nextEnd)

        else:
            currentInterval = interval
            result.append(currentInterval)

    return result


print(mergeIntervals([[1, 3], [2, 6], [8, 10], [9, 11]]))
