import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

arr = deque(range(1, N + 1))
answer = []

while True:
    if len(arr) == 0:
        break
    arr.rotate(-(K - 1))
    answer.append(arr.popleft())

print("<" + ", ".join(map(str, (answer))) + ">")
