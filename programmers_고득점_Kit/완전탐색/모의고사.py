def solution(answers):
    answer = []
    result = []
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    now = 1
    for supo in [supo_1, supo_2, supo_3]:
        score = 0
        supo_len = len(supo)
        for idx in range(len(answers)):
            if answers[idx] == supo[idx % supo_len]:
                score += 1
        result.append((now, score))
        now += 1
    maxV = 0
    answer = []
    for res in result:
        if res[1] > maxV:
            maxV = res[1]
            answer = [res[0]]
        elif res[1] == maxV:
            answer.append(res[0])
    return answer