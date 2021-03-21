def solution(numbers):
    numbers = list(map(list, map(str, numbers)))
    for number in numbers:
        if len(number) == 1:
            number.append(int(number[0]))
            number.append(int(number[0]))
            number.append(int(number[0]))
        elif len(number) == 2:
            number.append(int(number[0]))
            number.append(int(number[1]))
        else:
            number.append(int(number[0]))

    numbers = sorted(numbers, key=lambda x: (int(x[0]), int(x[1]), int(x[2]), int(x[3])), reverse=True)
    answer = ''
    for number in numbers:
        for ch in number:
            if type(ch) == type('string'):
                answer += ch

    return str(int(answer))