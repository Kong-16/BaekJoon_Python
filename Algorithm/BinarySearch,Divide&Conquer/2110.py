import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = []

for _ in range(N):
    house.append(int(input()))

house.sort()

start, end = 0, house[-1]

while start <= end:
    mid = (end + start) // 2
    next_dist = house[0] + mid
    cnt = 1
    for i in range(1, len(house)):
        if house[i] >= next_dist:
            cnt += 1
            next_dist = house[i] + mid
    if cnt < C:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
