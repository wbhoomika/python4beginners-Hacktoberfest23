"""
Merge sort takes in list and returns a sorted list
@author :Dharma Teja
more about merge sort https://en.wikipedia.org/wiki/Merge_sort
"""


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(a, b):
    sorted_arr = []
    i, j = 0, 0
    len_a = len(a)
    len_b = len(b)
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i += 1
        else:
            sorted_arr.append(b[j])
            j += 1
    while i < len_a:
        sorted_arr.append(a[i])
        i += 1
    while j < len_b:
        sorted_arr.append(b[j])
        j += 1
    return sorted_arr


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    sorted_ans = merge_sort(arr)
    for i in sorted_ans:
        print(i, end=" ")
