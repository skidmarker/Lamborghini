def solution(citations):
    citations.sort(reverse=True)
    total_cnt = len(citations)
    h = 0
    for i in range(total_cnt):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            return h

    return h