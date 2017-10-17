import os
import shutil


def main():
    os.chdir("FilesToSort")
    file_types = get_file_types(os.getcwd())
    # print(file_types)
    print(os.getcwd())

    for file_type in file_types:  # created directories by name of file extensions in unique set.
        os.mkdir(file_type)

    for filename in os.listdir(os.getcwd()):
        if "." in filename:
            file_extension = filename[filename.find(".") + 1:]
            shutil.move(filename, file_extension)


def get_file_types(directory):
    extensions = []
    for filename in os.listdir(directory):
        extension = filename[filename.find(".") + 1:]  # slices filename from first letter after the period to the end.
        extensions.append(extension)
    return set(extensions)  # returns a set of unique file types


main()
