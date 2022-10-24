import sys

input = sys.stdin.readline

N = int(input())

cnt = 99

if N < 100:
    cnt = N
elif N == 1000:
    cnt = 144
else:
    for i in range(100, N + 1):
        num = list(map(int, str(i)))
        if num[1] - num[0] == num[2] - num[1]:
            cnt += 1

print(cnt)
