import sys

input = sys.stdin.readline

N = int(input())
set = set()
arr = []
for _ in range(N):
    set.add(input().strip())

arr = list(set)
arr.sort(key=lambda arr: (len(arr), arr))

for i in arr:
    print(i)
