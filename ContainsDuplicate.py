def conatainsDuplicate(arr):
    duplicates = set()
    for num in arr:
        if num in duplicates:
            return True

        else:
            duplicates.add(num)

    return False



