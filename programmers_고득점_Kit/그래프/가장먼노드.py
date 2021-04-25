def solution(n, edge):
    answer = 0
    n_arr = [[] for _ in range(n+1)]
    for e in edge:
        n_arr[e[0]].append(e[1])
        n_arr[e[1]].append(e[0])
        
    queue = [1]
    visited = [0] * (n+1)
    visited[1] = 1
    
    maxV = 0
    maxN_cnt = 0
    while queue:
        node = queue.pop(0)
        for e in n_arr[node]:
            if visited[e] == 0:
                n_visited = visited[node] + 1
                if n_visited > maxV:
                    maxV = n_visited
                    maxN_cnt = 1
                elif n_visited == maxV:
                    maxN_cnt += 1
                queue.append(e)
                visited[e] = n_visited
    answer = maxN_cnt
    return answer