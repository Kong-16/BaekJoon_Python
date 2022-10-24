import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([y, x])

arr.sort()

for i in arr:
    print("{} {}".format(i[1], i[0]))
