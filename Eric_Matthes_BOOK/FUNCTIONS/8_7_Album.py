def make_album(artist_name, album_title, num_songs = None):
    album = {'name': artist_name, 'album': album_title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

album = make_album('Moby', '18', 20)
print(album)
