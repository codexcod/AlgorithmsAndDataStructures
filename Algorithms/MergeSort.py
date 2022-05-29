def arrayCopy(source,sourceStartingPoint,destination,destinationStartingPoint,size):
    destination[destinationStartingPoint:(destinationStartingPoint + size)] = source[sourceStartingPoint:(sourceStartingPoint + size)]

def mergeHalves(arr,temp, leftStart, rightEnd):
    #print("Left : " , leftStart," Right : ", rightEnd)
    leftEnd = (rightEnd + leftStart) // 2
    rightStart = leftEnd + 1
    size = rightEnd - leftStart + 1

    left = leftStart
    right = rightStart
    index = leftStart

    while left <= leftEnd and right <= rightEnd:
        if arr[left] <= arr[right]:
            temp[index] = arr[left]
            left += 1

        else:
            temp[index] = arr[right]
            right += 1

        index += 1

    arrayCopy(arr,left,temp,index,leftEnd-left+1)
    arrayCopy(arr,right,temp,index,rightEnd-right+1)
    arrayCopy(temp, leftStart, arr, leftStart,size)


def mergeSort(arr,temp,left,right):
    if left >= right:
        return

    middle = (left + right) // 2
    mergeSort(arr,temp,left,middle)
    mergeSort(arr,temp,middle + 1,right)
    #print("befor mergin : ",arr)
    mergeHalves(arr,temp,left,right)
    #print("after mergin : ", arr)

def sortArray(arr):
    mergeSort(arr, [0 for i in range(len(arr))] ,0, len(arr)-1)

arr = [3,2,1,7,4,9,2,10]
sortArray(arr)
print(arr)


