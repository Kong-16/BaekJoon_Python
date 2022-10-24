import sys

sys.setrecursionlimit(10**6)


N = int(sys.stdin.readline())

arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

for i in sorted(arr):
    print(i)
