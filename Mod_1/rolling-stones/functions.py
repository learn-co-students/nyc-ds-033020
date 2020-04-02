from collections import Counter

def find_by_name(data, album):
    for i in range(len(data)):
        if album == data[i]['album']:
            return data[i]
    return None

###ORIGINAL CODE###
# def find_by_name(album):
#     for i in range(len(new_list)):
#         if album == new_list[i]['album']:
#             return new_list[i]
#     return None

def find_by_rank(data, rank):
    for i in range(len(data)):
        if str(rank) == data[i]['number']:
            return data[i]
    return None

###ORIGINAL CODE###
# def find_by_rank(rank):
#     for i in range(len(new_list)):
#         if str(rank) == new_list[i]['number']:
#             return new_list[i]
#     return None

def find_by_year(data, year):
    return [album for album in data if str(year) == album['year']]
#     year_list = []
#     for i in range(len(data)):
#         if str(year) == data[i]['year']:
#             year_list.append(data[i])
#     return year_list

###ORIGINAL CODE###
# def find_by_year(year): 
#     year_list = []
#     for i in range(len(new_list)):
#         if str(year) == new_list[i]['year']:
#             year_list.append(new_list[i])
#     return year_list

def find_by_years(data, start_year, end_year):
    start = min(start_year,end_year)
    end = max(start_year,end_year)
    return [album for album in data if start <= int(album['year']) <= end]

#     year_list = []
#     for i in range(len(data)):
#         if ((int(data[i]['year']) >= start) & (int(data[i]['year']) <= end)):
#             year_list.append(data[i])
#     return year_list

###ORIGINAL CODE###
# def find_by_years(start_year,end_year):
#     start = min(start_year,end_year)
#     end = max(start_year,end_year)
#     year_list = []
#     for i in range(len(new_list)):
#         if ((int(new_list[i]['year'])>= start) & (int(new_list[i]['year'])<= end)):
#             year_list.append(new_list[i])
#     return year_list
    
def find_by_ranks(data, start_rank, end_rank):
    start = min(start_rank,end_rank)
    end = max(start_rank,end_rank)
    return [album for album in data if start <= int(album['number']) <= end]
#     rank_list = []
#     for i in range(len(data)):
#         if ((int(data[i]['number']) >= start) & (int(data[i]['number']) <= end)):
#             rank_list.append(data[i])
#     return rank_list

###ORIGINAL CODE###
# def find_by_ranks(start_rank, end_rank):  
#     start = min(start_rank,end_rank)
#     end = max(start_rank,end_rank)
#     rank_list = []
#     for i in range(len(new_list)):
#         if ((int(new_list[i]['number']) >= start) & (int(new_list[i]['number'])<= end)):
#             rank_list.append(new_list[i])
#         return rank_list
    
def album_titles(data):
    return [album['album'] for album in data]
    ###ORIGINAL CODE###
#     title_list = []
#     for i in range(len(data)):
#         title_list.append(data[i]['album'])
#     return title_list

def artists_inc_repeat(data):
    temp = [artist['artist'] for artist in data]
    return temp

def artists_unique(data):
    temp = [artist['artist'] for artist in data]
    return list(set(temp))
#     artist_list = []
#     for i in range(len(data)):
#         artist_list.append(data[i]['artist'])
#     return artist_list

def genres(data):
    temp = [artist['genre'] for artist in data]
    return list(set(temp))
#     genre_list = []
#     for i in range(len(data)):
#         genre_list.append(data[i]['genre'])
#     return genre_list

def most_albums(data):
    artist_rep_list = artists_inc_repeat(data)
    count_list = list(Counter(artist_rep_list).items())
    max_num = max([count[1] for count in count_list])
    return [count[0] for count in count_list if count[1] == max_num]

###ORIGINAL CODE###
# def most_albums(data):
#     artist_list = artists(data)
#     count = Counter(artist_list)
#     counted_list = list(count.items())
#     album_count_list = []
#     most_album_list = []
#     for i in range(len(counted_list)):
#         album_count_list.append(counted_list[i][1])
#     num = max(album_count_list)
#     for i in range(len(counted_list)):
#         if num == counted_list[i][1]:
#             most_album_list.append(counted_list[i][0])
#     return most_album_list

def most_words(data):
    album_list = album_titles(data)
    word_list = []
    for album in album_list:
        spt = album.split()
        word_list.extend(spt)
    count_list = list(Counter(word_list).items())
    max_num = max([count[1] for count in count_list])
    return [count[0] for count in count_list if count[1] == max_num]

###ORIGINAL CODE###
# def most_words(data):
#     album_list = album_titles(data)
#     word_list = []
#     most_word_list = []
#     word_count_list = []
#     most_frequent_word = []
#     #list of artists that have the most albums
#     for i in range(len(album_list)):
#         spt = album_list[i].split()
#         word_list.extend(spt)
#     most_word_list = Counter(word_list)
#     counted_list = list(most_word_list.items())
#     for i in range(len(counted_list)):
#         word_count_list.append(counted_list[i][1])
#     num = max(word_count_list)
#     for i in range(len(most_word_list)):
#         if num == counted_list[i][1]:
#             most_frequent_word.append(counted_list[i][0])
#     return most_frequent_word

def create_song_list(data):
    temp_list = [line.strip().split('\t') for line in data]
    song_dicts = [{'rank': temp[0],
                  'name': temp[1],
                  'artist': temp[2], 
                  'year': temp[3]} for temp in temp_list]
    return song_dicts

###ORIGINAL CODE###
# def create_song_list(data):
#     song_list = []
#     for song in data:
#         temp_list = song.split('\t')
#         song_list.append({'rank': temp_list[0],
#                           'name': temp_list[1],
#                           'artist': temp_list[2],
#                           'year': temp_list[3]})
#     return song_list

def album_with_most_top_songs(song_data,tracks_data):
    temp = []
    for song in song_data:
        for album in tracks_data:
            if song['name'] in album['tracks']:
                temp.append(album['album'])
                counted = list(Counter(temp).items())
    count_list = [count[1] for count in counted]
    num = max(count_list)
    album_top_songs = [album[0] for album in counted if num == album[1]]
    return album_top_songs

###ORIGINAL CODE###
# def album_with_most_top_songs():
#     temp = []
#     temp1 = []
#     temp2 = []
#     for song in ultimate_song_list:
#         for album in json_data:
#             if song['name'] in album['tracks']:
#                 temp.append(album['album'])
#                 count = list(Counter(temp).items())
#     for i in range(len(count)):
#         temp1.append(count[i][1])
#     num = max(temp1)
#     for i in range(len(count)):
#         if num == count[i][1]:
#             temp2.append(count[i][0])
#     return temp2

def albums_with_top_songs(song_data,tracks_data):
    temp = []
    for song in song_data:
        for album in tracks_data:
            if song['name'] in album['tracks']:
                temp.append(album['album'])
    return list(set(temp))

def songs_that_are_on_top_albums(song_data,tracks_data):
    temp = []
    for song in song_data:
        for album in tracks_data:
            if song['name'] in album['tracks']:
                temp.append(song['name'])
    return list(set(temp))