def solution(prices):
    answer = []
    stock_dict = {}
    for i in range(len(prices)):
        stock_dict[i] = 0
    
    for i in range(len(prices)-2):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(j-i)
    answer += [1, 0]
    
    return answer