def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    start = -30001
    for route in routes:
        if start < route[0]:
            answer += 1
            start = route[1]

    return answer