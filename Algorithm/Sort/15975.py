import sys

input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N)]

for _ in range(N):
    p, c = map(int, input().split())
    arr[c].append(p)

for i in arr:
    i.sort()

new_arr = []
rem_arr = []

print(arr)
