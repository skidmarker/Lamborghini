import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    while True:
        if heap[0] >= K:
            break
        first = heapq.heappop(heap)
        if len(heap) == 0:
            return -1
        second = heapq.heappop(heap)
        new_scoville = first + second * 2
        heapq.heappush(heap, new_scoville)
        answer += 1
        
    return answer