import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a = deque()
    success = True
    str = input()
    for i in str:
        if i == "(":
            a.append(i)
        elif i == ")":
            try:
                a.pop()
            except:
                success = False
                break
    if a or success == False:
        print("NO")
    else:
        print("YES")
