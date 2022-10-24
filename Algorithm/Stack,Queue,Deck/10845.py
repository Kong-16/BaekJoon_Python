import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
a = deque()

for _ in range(N):
    str = input()
    try:
        command, num = str.split()
    except:
        command = str.strip()

    if command == "push":
        a.append(num)
    elif command == "pop":
        try:
            print(a.popleft())
        except:
            print(-1)
    elif command == "front":
        try:
            print(a[0])
        except:
            print(-1)
    elif command == "back":
        try:
            print(a[len(a) - 1])
        except:
            print(-1)
    elif command == "size":
        print(len(a))
    elif command == "empty":
        if a:
            print(0)
        else:
            print(1)
