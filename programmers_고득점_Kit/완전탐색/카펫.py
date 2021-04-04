def solution(brown, yellow):
    answer = []
    total = brown + yellow
    cross_set = set()
    for i in range(2, total-1):
        if total % i == 0:
            j = total // i
            hor = max(i, j)
            ver = min(i, j)
            border = (hor + ver) * 2 - 4
            center = total - border
            if border == brown and center == yellow:
                answer = [hor, ver]
                break
    return answer