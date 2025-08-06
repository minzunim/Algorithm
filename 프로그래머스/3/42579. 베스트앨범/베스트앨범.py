def solution(genres, plays):
    # 장르별로 가장 많이 재생된 노래 2개씩
    # 많이 재생된 장르를 먼저
    # 장르 = key, 재생횟수 = value인 맵 하나 -> 둘중에 고름
    # 장르 내 많이 재생된 노래를 먼저
    # 앞에서 뽑힌 장르의 노래만 골라서 플레이 맵
    # 개수 많은 거 2개까지
    # 같은 장르 안에서 재생 횟수가 같으면 고유 번호가 낮은 노래
    genre_map = {}
    
    for genre, play in zip(genres, plays):
        if genre not in genre_map:
            genre_map[genre] = play
        else:
            genre_map[genre] += play 
    # { classic : 1000, pop, 1500 }
            
    # genre_map에서 play가 높은 쪽을 선택
    genre_map = sorted(genre_map.items(), key= lambda item:item[1], reverse=True) # 내림차순 정렬

    # 장르, 재생수, 고유번호 리스트로 저장
    songs = []
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        songs.append((genre, play, i))
            
    # 장르별로 노래 모으고 정렬
    from collections import defaultdict
        
    genre_to_songs = defaultdict(list)
    for genre, play, idx in songs:
        genre_to_songs[genre].append((play, idx))
    
    # print(genre_to_songs)

    # 장르별로 재생수 내림차순, 고유번호 오름차순 정렬
    for genre in genre_to_songs:
        genre_to_songs[genre].sort(key=lambda x: (-x[0], x[1]))
        
    answer = []
    for genre, _ in genre_map:  # 많이 재생된 장르부터
        for play, idx in genre_to_songs[genre][:2]:
            answer.append(idx)
            
    return answer
    
                