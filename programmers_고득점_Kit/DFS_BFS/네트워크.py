def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        queue = [i]
        visited.add(i)
        while queue:
            node = queue.pop(0)
            for j in range(n):
                if computers[node][j] == 1 and j not in visited:
                    visited.add(j)
                    queue.append(j)
        answer += 1
    return answer