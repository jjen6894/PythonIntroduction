imelda = "More Mayhem", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda

# (track_1, track_2, track_3, track_4) = tracks
# track_number_1, track_title_1 = track_1
# track_number_2, track_title_2 = track_2
# track_number_3, track_title_3 = track_3
# track_number_4, track_title_4 = track_4
# print(title, artist, year)
# print(track_number_1, ' ', track_title_1)
# print(track_number_2, ' ', track_title_2)
# print(track_number_3, ' ', track_title_3)
# print(track_number_4, ' \t', track_title_4)

for song in tracks:
    track, title = song
    print('\t', song)
    print("\tTrack Number {}, Title: {}".format(track, title))

