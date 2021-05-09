def solution(n, results):
    answer = 0
    result_dict = dict()
    for i in range(1, n + 1):
        result_dict[i] = {
            'win': set(),
            'lose': set()
        }

    for result in results:
        winner = result[0]
        loser = result[1]
        result_dict[winner]['win'].add(loser)
        result_dict[loser]['lose'].add(winner)

    for i in range(1, n+1):
        for loser in list(result_dict[i]['win']):
            result_dict[loser]['lose'] = result_dict[loser]['lose'] | result_dict[i]['lose']
        for winner in list(result_dict[i]['lose']):
            result_dict[winner]['win'] = result_dict[winner]['win'] | result_dict[i]['win']

    for i in range(1, n + 1):
        total = 0
        total += len(result_dict[i]['win'])
        total += len(result_dict[i]['lose'])
        if total == n - 1:
            answer += 1

    return answer