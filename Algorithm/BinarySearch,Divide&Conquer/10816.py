import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

count = {}
answer = []

for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in find:
    n = count.get(i)
    if n == None:
        n = 0
    answer.append(n)

for i in answer:
    print(i, end=" ")
