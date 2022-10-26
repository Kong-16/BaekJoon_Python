import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

coins = []
for _ in range(N):
    coins.append(int(input()))

coins.reverse()

cnt = 0
for i in coins:
    if K >= i:
        while K >= i:
            cnt += 1
            K -= i

print(cnt)
