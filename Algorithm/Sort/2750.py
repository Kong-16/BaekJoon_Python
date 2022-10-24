import sys
sys.setrecursionlimit(10**6)

N = int(input())

arr = []


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    L, P, R = [], [], []
    for i in arr:
        if i < pivot:
            L.append(i)
        elif i > pivot:
            R.append(i)
        else:
            P.append(i)
    return quick_sort(L) + P + quick_sort(R)


for i in range(N):
    arr.append(int(input()))

arr = quick_sort(arr)

for i in arr:
    print(i)