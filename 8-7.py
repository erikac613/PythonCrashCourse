def make_album(artist_name, album_title, tracks=''):
    artist_and_album = {'artist': artist_name, 'title': album_title}
    if tracks:
        artist_and_album['tracks'] = tracks
    return artist_and_album

music_info = make_album('beck', 'odelay')
print(music_info)

music_info = make_album('kate bush', 'the kick inside')
print(music_info)

music_info = make_album('neil young', 'after the gold rush')
print(music_info)

music_info = make_album('coheed and cambria', 'the second stage turbine blade', tracks=12)
print(music_info)
