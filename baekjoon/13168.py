n, r = map(int, input().split())
cities = input().split()
cost = [[[float('INF'), float('INF')] for _ in range(n)] for _ in range(n)]
cityMap = dict()

for i in range(n):
    cityMap[cities[i]] = i
    cost[i][i] = [0, 0]

m = int(input())
visits = input().split()
k = int(input())
for _ in range(k):
    kind, a, b, w = input().split()
    a, b = cityMap[a], cityMap[b]
    w = int(w)
    cost[a][b][1] = cost[b][a][1] = min(cost[a][b][1], w)
    if kind in ['S-Train', 'V-Train']:
        w /= 2
    elif kind in ["Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"]:
        w = 0
    cost[a][b][0] = cost[b][a][0] = min(cost[a][b][0], w)

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j][0] = cost[j][i][0] = min(
                cost[i][j][0], cost[i][k][0]+cost[k][j][0])
            cost[i][j][1] = cost[j][i][1] = min(
                cost[i][j][1], cost[i][k][1]+cost[k][j][1])

start, t1, t2 = cityMap[visits[0]], 0, 0
for i in range(1, m):
    nx = cityMap[visits[i]]
    t1 += cost[start][nx][0]
    t2 += cost[start][nx][1]
    start = nx

if t1+r < t2:
    answer = 'Yes'
else:
    answer = 'No'
print(answer)