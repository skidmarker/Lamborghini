def solution(triangle):
    answer = 0
    result = [triangle[0]]
    for i in range(1, len(triangle)):
        target = triangle[i]
        temp = [0] * (i + 1)
        for j in range(i + 1):
            left = target[j]
            right = target[j]
            if j - 1 >= 0:
                left = result[i-1][j-1] + target[j]
            if j < i:
                right = result[i-1][j] + target[j]
            temp[j] = max(left, right)
        result.append(temp)
    answer = max(result[-1])
    return answer