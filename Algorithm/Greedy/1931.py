from re import X
import sys

input = sys.stdin.readline

N = int(input())

time_table = []

for _ in range(N):
    time_table.append(list(map(int, input().split())))

time_table.sort()
time_table.sort(key=lambda x: x[1])

cnt = 0

end = 0

for meeting in time_table:
    if end <= meeting[0]:
        cnt += 1
        end = meeting[1]

print(cnt)
