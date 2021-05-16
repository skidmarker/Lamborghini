def main():
    r, c = map(int, input().split())
    field = [input() for _ in range(r)]
    visited = set()
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sheep_cnt = 0
    wolf_cnt = 0
    for i in range(r):
        for j in range(c):
            if (i, j) not in visited and field[i][j] != '#':
                wolf = 0
                sheep = 0
                visited.add((i, j))
                queue = [(i, j)]

                while queue:
                    ti, tj = queue.pop(0)
                    if field[ti][tj] == 'o':
                        sheep += 1
                    elif field[ti][tj] == 'v':
                        wolf += 1
                    for d in delta:
                        ni = ti + d[0]
                        nj = tj + d[1]
                        if 0 <= ni < r and 0 <= nj < c and (ni, nj) not in visited and field[ni][nj] != '#':
                            queue.append((ni, nj))
                            visited.add((ni, nj))

                if sheep > wolf:
                    sheep_cnt += sheep
                else:
                    wolf_cnt += wolf
    print(sheep_cnt, wolf_cnt)

if __name__=="__main__":
    main()