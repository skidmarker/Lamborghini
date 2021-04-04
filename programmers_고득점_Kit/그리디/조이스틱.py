def solution(name):
    answer = 0
    target_arr = []
    target_dict = dict()
    for i in range(len(name)):
        if name[i] != 'A':
            target_arr.append(i)
            target_dict[i] = False
    now_pos = 0
    target_cnt = len(target_arr)
    while target_cnt > 0:
        minV = len(name)
        next_ch = 0
        for target in target_arr:
            if target_dict[target] == False:
                dis = min(abs(target - now_pos), len(name) - abs(target - now_pos))
                if dis < minV:
                    minV = dis
                    next_ch = target

        answer += minV
        now_pos = next_ch
        ch = name[next_ch]
        ch_change = min(ord(ch) - ord('A'), (ord('Z') - ord(ch) + 1))
        answer += ch_change
        target_dict[next_ch] = True
        target_cnt -= 1

    return answer