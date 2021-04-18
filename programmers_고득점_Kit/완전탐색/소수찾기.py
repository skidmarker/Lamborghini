from itertools import permutations

def solution(numbers):
    answer = 0
    def f(n):
        if n < 2: 
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    numbers = list(numbers)
    ans_set = set()
    for i in range(1, len(numbers)+1):
        permutation = permutations(numbers, i)
        for p in permutation:
            new_number = int(''.join(p))
            if new_number not in ans_set:
                ans_set.add(new_number)
                if f(new_number):
                    answer += 1
    return answer