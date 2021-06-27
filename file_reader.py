import json

file_name = "songs.json"
file_ptr = open(file_name, "r")
songs_dict = json.load(file_ptr)
all_songs = songs_dict.get("songlist")

playlist = list()
while True:
    counter = 1
    print("Here are all songs")

    for songs in all_songs:
        
        title = songs.get("title")
        artist = songs.get("artist")
        print(counter,".",title,"is by",artist)
        counter+=1

    
    num_input = int(input("Enter which songs you want. "))
        
    if num_input > len(all_songs):
        print("Number out of range, Try again")
        num_input = int(input("Enter which songs you want. "))
        
        
    song_chosen = all_songs[num_input - 1]

    title = song_chosen.get("title")
    artist = song_chosen.get("artist")
    
    print(title, "by", artist, "has been added to playlist")
    
        
    song = list()
    song.append(title)
    song.append(artist)
    playlist.append(song)

    try:
        user_input = input("Choose another song? Y or N ").upper()
        
    except(ValueError):
        print("Input Invalid, Try again")
        continue
        
    if user_input == "N":
        break
    else:
        continue
    print("playlist: ",playlist)

output_ptr = open("playlist.csv","w")
output_ptr.write("number, title, artist\n")

counter = 1

for song in playlist:
    output_ptr.write(str(counter) + "," + song[0] + "," + song[1] + '\n')
    counter+=1

output_ptr.close()