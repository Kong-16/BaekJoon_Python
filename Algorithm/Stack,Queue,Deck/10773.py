import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
a = deque()

for _ in range(K):
    num = int(input())
    if num:
        a.append(num)
    else:
        a.pop()

print(sum(a))
