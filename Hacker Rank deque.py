from collections import deque

N = int(input())
d = deque()

for _ in range(N):
    operation, *values = input().split()

    if operation == "append":
        d.append(int(values[0]))
    elif operation == "appendleft":
        d.appendleft(int(values[0]))
    elif operation == "pop":
        d.pop()
    elif operation == "popleft":
        d.popleft()


print(*d)
