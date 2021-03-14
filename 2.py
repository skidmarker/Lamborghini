def solution(numbers):
    numbers = list(map(list, map(str, numbers)))
    for number in numbers:
        while len(number) < 3:
            number.append(int(number[0]))

    numbers = sorted(numbers, key=lambda x: (int(x[0]), int(x[1]), int(x[2])), reverse=True)
    answer = ''
    for number in numbers:
        for ch in number:
            if type(ch) == type('string'):
                answer += ch

    return str(int(answer))