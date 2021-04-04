def solution(n, costs):
    answer = 0
    p = list(range(n))
    
    def find(n):
        if n != p[n]:
            p[n] = find(p[n])
        return p[n]
    
    def union(u, v):
        parent_1 = find(u)
        parent_2 = find(v)
        p[parent_2] = parent_1
        
    costs.sort(key=lambda x: x[2])
    
    for cost in costs:
        node_1 = cost[0]
        node_2 = cost[1]
        
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            answer += cost[2]
            
    return answer