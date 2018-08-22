def insert_sort(l):
    for i in range(1, len(l)):
        curr = l[i]
        for j in range(0, i)[::-1]:
            if curr < l[j]:
                l[j + 1] = l[j]
                l[j] = curr
    return l

def shell_sort(l):
    length = len(l)
    step = 2
    group = length / step
    while group > 0:
        for i in range(group):
            j = i + group
            while j < length:
                k = j - group
                curr = l[j]
                while k >= 0:
                    if l[k] > curr:
                        l[k + group] = l[k]
                        l[k] = curr
                    k -= group
                j += group
        group /= step
    return l

def bubble_sort(l):
    length = len(l)
    for i in range(0, length):
        for j in range(i + 1, length):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

def quick_sort(l, left, right):
    if left >= right:
        return l
    key = l[left]
    start = left
    end = right
    while left < right:
        while left < right and l[right] >= key:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] <= key:
            left += 1
        l[right] = l[left]
    l[right] = key
    quick_sort(l, start, left - 1)
    quick_sort(l, left + 1, end)
    return l

def selection_sort(l):
    length = len(l)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if l[j] < l[min]:
                min = j
        l[min], l[i] = l[i], l[min]
    return l

def adjust_heap(l, i, size):
    ''' adjust the heap with a given size from the i-th node '''
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    max = i
    if i < size / 2: # i should be a inner node
        if leftChild < size and l[leftChild] > l[max]:
            max = leftChild
        if rightChild < size and l[rightChild] > l[max]:
            max = rightChild
        if max != i:
            l[max], l[i] = l[i], l[max]
            adjust_heap(l, max, size)

def heap_sort(l):
    size = len(l)
    # build a heap
    for i in range(size / 2)[::-1]:
        adjust_heap(l, i, size)
    for i in range(size)[::-1]:
        l[0], l[i] = l[i], l[0]
        adjust_heap(l, 0, i)
    return l

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(l):
    if len(l) <= 1:
        return l
    split = len(l) / 2
    left = merge_sort(l[:split])
    right = merge_sort(l[split:])
    return merge(left, right)

def radix_sort2(l):
    import math
    radix = 10
    k = int(math.ceil(math.log(max(l), radix)))
    print k
    bucket = [[] for i in range(radix)]
    for i in range(k):
        for item in l:
            bucket[item / (radix ** i) % radix].append(item)
        del l[:]
        for each in bucket:
            l.extend(each)
        bucket = [[] for i in range(radix)]
    return l

def countingSort(arr, exp1):
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[(index) % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radix_sort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
    return arr
 
 
if __name__ == '__main__':
    l = [10,5,4,3,1,8,7,9]
    print(insert_sort(l))
    print(shell_sort(l))
    print(bubble_sort(l))
    print(quick_sort(l, 0, len(l) - 1))
    print(selection_sort(l))
    print(heap_sort(l))
    print(merge_sort(l))
    print(radix_sort(l))