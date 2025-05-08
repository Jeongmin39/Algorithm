from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    song_dict = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        song_dict[genre].append((i, play))

    sorted_genres = sorted(song_dict.items(), key = lambda x: sum(val[1] for val in x[1]), reverse = True)
    
    for genre, song in sorted_genres:
        song.sort(key = lambda x: (-x[1], x[0]))
        top_songs = song[:2]
        answer.extend([idx for idx, play in top_songs])
        
    return answer