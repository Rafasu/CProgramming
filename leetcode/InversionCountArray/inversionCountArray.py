def mergeSplit(array, start, middle, end):
    temp = []
    inversionCount = 0
    i, j, k = start, middle + 1, 0
    while(i <= middle and j <= end):
        if(array[i] <= array[j]):
            temp.append(array[i])
            i += 1
        else:
            inversionCount += middle - i + 1
            temp.append(array[j])
            j += 1
    while(i <= middle):
        temp.append(array[i])
        i += 1
    while(j <= end):
        temp.append(array[j])
        j += 1
    for i in range(start, end+1):
        array[i] = temp[i-start]
            
    return inversionCount

def mergeCount(array, start, end):
    inversionCount = 0
    if( start < end):
        middle = (start + end)//2
        inversionCount += mergeCount(array, start, middle)
        inversionCount += mergeCount(array, middle+1, end)
        inversionCount += mergeSplit(array, start, middle, end)
    return inversionCount
    
array = [1, 9, 6, 4, 5]
print (array)
numberInversions = mergeCount(array, 0, len(array)-1)
print("Count of Inversions: %d" % numberInversions)
# Bibliography: https://www.techiedelight.com/inversion-count-array/

# Copy of another implementation down below:

def merge(array, temp, left, mid, right):
    k, i, j = left, left, mid + 1
    count = 0
    while i <= mid and j <= right:
        if array[i] > array[j]:
            count += mid - i + 1
            temp[k] = array[j]
            j += 1
        else:
            temp[k] = array[i]
            i += 1
        k += 1

    while i <= mid:
        temp[k] = array[i]
        i += 1
        k += 1
    for i in range(left, right+1):
        array[i] = temp[i]
    return count


def mergeSort(array, temp, left, right):
    if left == right:
        return 0
    mid = int((left + right) / 2)
    count = 0
    count += mergeSort(array, temp, left, mid)
    count += mergeSort(array, temp, mid + 1, right)
    count += merge(array, temp, left, mid, right)
    return count


if __name__ == '__main__':
    array = [1, 8, 5]
    temp = list(array)
    print(mergeSort(array, temp, 0, len(array)-1))
