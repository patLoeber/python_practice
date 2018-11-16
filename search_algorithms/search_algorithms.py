# worst and avg: O(n^2)
# best:  O(n)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i

        # while j > 0 and A[j-1] < cur: for decreasing order
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = cur


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


# worst and avg: O(n^2)
# best: O(n)
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)


def fast_bubble_sort(arr):
    exchanges = True
    i = len(arr)-1
    while i > 0 and exchanges:
        exchanges = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                exchanges = True
                swap(arr, j, j+1)

a = [1, 2, 0, 1, 0]
insertion_sort(a)
print(a)

b = [1, 3, 2, 7, 9, 1, 2]
# bubble_sort(b)
fast_bubble_sort(b)
print(b)

