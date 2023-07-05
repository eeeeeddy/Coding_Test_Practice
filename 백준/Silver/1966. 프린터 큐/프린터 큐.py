import sys
from collections import deque

x = int(input())

for i in range(x):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    order = deque(i for i in range(len(queue)))
    answer = deque()
    answer_order = deque()
    
    while len(queue) >= 1:
        if queue[0] == max(queue):
            answer.append(queue.popleft())
            answer_order.append(order.popleft())
        else:
            queue.append(queue.popleft())
            order.append(order.popleft())

    print(answer_order.index(m) + 1)