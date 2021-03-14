def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        target_array = sorted(array[i-1 : j])
        answer.append(target_array[k-1])
    return answer