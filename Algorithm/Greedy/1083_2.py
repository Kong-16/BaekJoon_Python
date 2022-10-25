import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = int(input())

it = 0

while it <= (len(A) - 1):
    mx = max(A[it : it + S + 1])
    idx = A.index(mx)
    for i in range(idx, it, -1):
        A[i], A[i - 1] = A[i - 1], A[i]
    S -= idx - it
    it += 1
    if S <= 0:
        break

print(*A)
