import os
import shutil

FILE_CATEGORY_STATEMENT = "How do you want to categorize {} files?: "


def main():
    os.chdir("FilesToSort2")
    file_types = get_file_types(os.getcwd())
    file_categories = user_organize_files(file_types)
    for file_category in file_categories:
        os.mkdir(file_category)
    for filename in os.listdir(os.getcwd()):
        if "." in filename:
            file_extension = filename[filename.find(".") + 1:]
            for file_group, file_type in file_categories.items():
                if file_extension in file_type:
                    shutil.move(filename, file_group)


def get_file_types(directory):
    extensions = []
    for filename in os.listdir(directory):
        extension = filename[filename.find(".") + 1:]  # slices filename from first letter after the period to the end.
        extensions.append(extension)
    return set(extensions)  # returns a set of unique file types


def user_organize_files(file_types):
    """Allows the user to create dict keys to categorise their document types."""
    user_file_groups = {}
    for file_type in file_types:
        user_choice = input(FILE_CATEGORY_STATEMENT.format(file_type)).title()
        if user_choice not in user_file_groups:
            user_file_groups[user_choice] = []
            user_file_groups[user_choice].append(file_type)
        else:
            user_file_groups[user_choice].append(file_type)
    return user_file_groups

main()
