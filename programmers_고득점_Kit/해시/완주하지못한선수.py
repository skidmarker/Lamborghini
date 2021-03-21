def solution(participant, completion):
    p_dict = dict()
    for p in participant:
        if p not in p_dict:
            p_dict[p] = 1
        else:
            p_dict[p] += 1
    for c in completion:
        if c in p_dict:
            p_dict[c] -= 1
    
    for key, value in p_dict.items():
        if value > 0:
            return key