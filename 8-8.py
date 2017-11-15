def make_album(artist_name, album_title, tracks=''):
    artist_and_album = {'artist': artist_name, 'title': album_title}
    if tracks:
        artist_and_album['tracks'] = tracks
    return artist_and_album

artist = ''
album = ''

while True:
    print("\nPlease enter a musician's name and the name of an album by that musician.")
    print("(enter 'q' at any time to quit)")

    input1 = raw_input("Artist's name: ")
    if input1 == 'q':
        break
    else:
        artist = input1

    input2 = raw_input("Album: ")
    if input2 == 'q':
        break
    else:
        album = input2

print(artist)
print(album)

music_info = make_album(artist, album)
print(music_info)
