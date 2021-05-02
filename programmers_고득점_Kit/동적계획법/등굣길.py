def solution(m, n, puddles):
    field = [[0] * m for _ in range(n)]
    
    field[0][0] = 1

    for puddle in puddles:
        field[puddle[1] - 1][puddle[0] - 1] = -1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0 or field[i][j] == -1:
                continue
            top = 0
            left = 0
            if i-1 >= 0 and field[i - 1][j] != -1:
                top = field[i - 1][j]
            if j-1 >= 0 and field[i][j - 1] != -1:
                left = field[i][j - 1]
            field[i][j] = top + left
    answer = field[-1][-1] % 1000000007
    return answer