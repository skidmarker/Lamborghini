def solution(number, k):
    answer = ''
    target = set()
    for i in range(1, len(number)):
        if int(number[i]) > int(number[i-1]):
            pos = i-1
            while True:
                if int(number[pos]) < int(number[i]):
                    target.add(pos)
                else:
                    break
                if k == len(target):
                    break
                pos -= 1
                if pos < 0:
                    break
            if k == len(target):
                break
    for idx in range(len(number)):
        if idx not in target:
            answer += number[idx]
    if k != len(target) and answer[-1] < answer[-2]:
        answer = answer[:-1]
    return answer