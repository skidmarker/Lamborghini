def solution(genres, plays):
    answer = []
    music_dict = dict()
    for i in range(len(genres)):
        genre = genres[i]
        if genre not in music_dict:
            music_dict[genre] = [[i], plays[i]]
        else:
            music_dict[genre][0].append(i)
            music_dict[genre][1] += plays[i]
    sorted_music_for_total_play_per_genre = []
    
    for value in music_dict.values():
        temp1 = sorted(value[0], key=lambda x : plays[x], reverse=True)
        temp2 = value[1]
        sorted_music_for_total_play_per_genre.append((temp1, temp2))
    
    sorted_music_for_total_play_per_genre.sort(key=lambda x : x[1], reverse=True)
    
    for sorted_genre in sorted_music_for_total_play_per_genre:
        answer += sorted_genre[0][:2]
        
    return answer