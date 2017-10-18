import os


def main():
    copyright_free_songs = {}
    os.chdir("Lyrics")

    for directory in os.listdir("."):
        os.chdir(directory)  # Moves into the required sub-directory.
        copyright_free_songs[directory] = []

        for file in os.listdir("."):
            in_file = open(file)
            if ".i " not in in_file.read():
               copyright_free_songs[directory].append(file)

        os.chdir("..")  # Moves up one directory to allow os.chdir() to reassign correct directory.

    for song_group, songs in copyright_free_songs.items():
        print("\n**{}**".format(song_group))
        for song in songs:
            print(song)

# def find_copyright_free_songs():


main()
