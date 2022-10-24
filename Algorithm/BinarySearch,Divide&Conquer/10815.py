import sys

input = sys.stdin.readline


def BinarySearch(arr, start, end, num):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] < num:
        return BinarySearch(arr, mid + 1, end, num)
    elif arr[mid] > num:
        return BinarySearch(arr, start, mid - 1, num)
    else:
        return True


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))
answer = []

cards.sort()

for i in find:
    if BinarySearch(cards, 0, len(cards) - 1, i):
        print(1, end=" ")
    else:
        print(0, end=" ")

