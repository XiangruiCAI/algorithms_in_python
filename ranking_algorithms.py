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


if __name__ == '__main__':
    l = [10,5,4,3,1,8,7,9]
    print(insert_sort(l))
    print(shell_sort(l))
    print(bubble_sort(l))
    print(quick_sort(l, 0, len(l) - 1))