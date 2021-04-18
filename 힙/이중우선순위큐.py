def solution(operations):
    answer = []
    heap = []
    for op in operations:
        if op[0] == 'I':
            num = int(op.split()[1])
            heap.append(num)
            heap.sort()
        else:
            op = int(op.split()[1])
            if op == 1:
                heap = heap[:-1]
            else:
                heap = heap[1:]

    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [heap[-1], heap[0]]
    return answer