# Sort
import sys

input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(N):
    p, c = map(int, input().split())
    arr[c].append(p)

sorted_arr = [i for i in arr if len(i) > 1]
for i in sorted_arr:
    i.sort()

dis_sum = 0
for i in sorted_arr:
    for j in range(len(i)):
        if j == 0:
            dis_sum += i[j + 1] - i[j]
        elif j == len(i) - 1:
            dis_sum += i[j] - i[j - 1]
        else:
            dis_sum += min(i[j] - i[j - 1], i[j + 1] - i[j])

print(dis_sum)
