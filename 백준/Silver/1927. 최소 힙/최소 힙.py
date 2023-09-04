import sys, heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:                  # x가 0이 아닐 경우에 heap에 추가
        heapq.heappush(heap, x) 
    else:
        if len(heap) == 0:      # heap이 비어있을 경우 0을 출력
            print(0)
        else:                   # heap에 값이 있을 경우 가장 작은 값을 출력하고 그 값을 삭제
            print(heap[0])      
            heapq.heappop(heap)