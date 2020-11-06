def make_album(artist, title, tracks = None):
    """Build a dictionary containing inf about an album"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
         album_dict['tracks'] = tracks
    return album_dict
# Prepare the prompts
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

#Let the user know how to quit
print("Enter 'quit' to stop ")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)
print("\nThanks for responding!")