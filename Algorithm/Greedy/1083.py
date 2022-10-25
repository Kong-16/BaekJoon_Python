import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

S = int(input())

B = A.copy()
B.sort()

cnt = 0
it = 0

while len(B) > 0 and S > 0:
    big = B.pop()
    idx = A.index(big)
    if idx - it <= S:
        S -= idx - it
        for i in range(idx, it, -1):
            A[i], A[i - 1] = A[i - 1], A[i]
        it += 1

print(*A)
