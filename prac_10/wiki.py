import wikipedia


def main():
    finished = False
    while not finished:
        search_key = input("Search >>> ")
        if not search_key:
            finished = True
        else:
            wiki_page = search(search_key)
            print(wikipedia.summary(wiki_page), "\nDo you want the page details? y/n")
            user_page_request = input(">>>").lower().strip()
            if user_page_request == "y":
                wiki_page_details = wikipedia.page(wiki_page)
                print("Title: {}\nURL: {}\n{}".format(wiki_page_details.title, wiki_page_details.url,
                                                      wiki_page_details.content))
    print("Farewell knowledge seeker.")


def search(phrase):
    """Lists only correct wikipedia pages and returns a user page choice."""
    search_options = wikipedia.search(phrase)
    for index, search_option in enumerate(search_options):
        print("{} --> {}".format(index, search_option))
    choice = int(input("Please choose an option"))
    return search_options[choice]


main()
