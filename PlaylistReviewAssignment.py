# William Meares
# Computer Programming
# Period 4
# 9/21/2026

playlist = ["Twinkle Twinkle", "ABC song", "Let it go", "Brandy"]
new_song = input("Add your favorite song: ")
new_song.strip()
new_song.title()
playlist.append(new_song)
print(len(playlist))
playlist.insert(0, "Rudolph the red nosed raindeer")
playlist.remove("ABC song")
del(playlist[2])
print(sorted(playlist))
playlist.sort()
playlist.reverse()
print("Brandy" in playlist)
for song in playlist:
    print(song.upper())
for i in range(len(playlist)):
    print(i+1, playlist[i])