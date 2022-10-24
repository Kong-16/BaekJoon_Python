import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

minimum = 1000000000
for i in range(len(arr)):
    