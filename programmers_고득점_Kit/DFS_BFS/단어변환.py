def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    word_len = len(begin)
    queue = [begin]
    visited = {begin: 0}
    while queue:
        start = queue.pop(0)
        temp = []
        for word in words:
            if word in visited:
                continue
            diff_cnt = 0
            for i in range(word_len):
                if start[i] != word[i]:
                    diff_cnt += 1
            if diff_cnt == 1:
                if word == target:
                    return visited[start] + 1
                queue.append(word)
                visited[word] = visited[start] + 1
            else:
                temp.append(word)
        words = temp