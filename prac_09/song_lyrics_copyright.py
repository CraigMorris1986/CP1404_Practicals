import os


def main():
    copyright_free_songs = {}
    os.chdir("Lyrics")

    for directory in os.listdir("."):
        os.chdir(directory)  # Moves into the required sub-directory.
        non_copyright_songs = find_copyright_free_songs()
        copyright_free_songs[directory] = non_copyright_songs
        os.chdir("..")  # Moves up one directory to allow os.chdir() to reassign correct directory.

    for song_group, songs in copyright_free_songs.items():
        print("\n**{}**".format(song_group))
        for song in songs:
            print(song)


def find_copyright_free_songs():
    """Searches each file in CWD for the copyright marker and returns a list of files that don't contain it."""
    searched_songs = []
    for file in os.listdir("."):
        in_file = open(file)
        if ".i " not in in_file.read():
            searched_songs.append(file)
    return searched_songs


main()
