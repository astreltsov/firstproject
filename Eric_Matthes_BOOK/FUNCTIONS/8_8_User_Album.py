def make_album(artist_name, album_title, num_songs = None):
    album = {'name': artist_name, 'album': album_title}
    # if num_songs:
    #     album['num_songs'] = num_songs
    return album
while True:
    print("Please tell me your artist name and album title")
    print("\n(enter 'q' if you want to quit)")
    name = input("\nArtist name: ")
    if name == 'q':
        break
    album = input("\nAlbum name: ")
    if album == 'q':
        break
    else:
        result = make_album(name, album)
        print(result)