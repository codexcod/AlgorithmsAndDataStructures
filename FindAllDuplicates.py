def findAllDuplicates(array):
    seen = set()
    result = []
    for num in array:
        if num in seen:
            result.append(num)

        seen.add(num)

    return result


def findAllDuplicatesNoMemory(array):
    result = []
    for num in array:
        if array[num - 1] < 0:
            result.append(num)

        array[num - 1] = -array[num - 1]

    return result

