# Handling user commands: search by keyword, search by genre and year, and show popular queries
import db_operations
import display
from colorama import Fore, Style

# Function to handle searching movies by a keyword
def handle_search_by_keyword():
    # Prompt the user to enter a keyword for the search
    keyword = input(Fore.BLUE + "\n✅ Enter the keyword for search: ")
    # Search for movies matching the keyword in the database (title and description)
    movies = db_operations.search_movies_by_keyword(keyword)
    # Save the search query for future analytics
    db_operations.save_search_query('keyword', keyword)
    # Display the results if any movies are found
    if movies:
        display.show_movies(movies)
    else:
        # Show a "no results" message if nothing is found
        display.show_no_results()

# Function to handle searching movies by genre and release year
def handle_search_by_genre_and_year():
    # Get the list of valid genres from the database
    genres = db_operations.get_valid_categories()
    print(Fore.MAGENTA + "\n🎬 Available genres:")
    # Display the list of genres with an index number
    for idx, genre in enumerate(genres, 1):
        # genre[0] extracts the genre name from the tuple
        print(f"{idx}. {genre[0]}")

    # Prompt the user to select a genre
    while True:
        try:
            genre_index = int(input(Fore.BLUE + f"\n✅ Choose genre (1-{len(genres)}): " + Style.RESET_ALL))
            if 1 <= genre_index <= len(genres):
                # Extract the genre name from the selected index
                genre = genres[genre_index - 1][0] # genre[0] - to extract string from tuple
                break
            else:
                # Handle invalid genre selection
                print(Fore.YELLOW + "Invalid genre selection. Please try again." + Style.RESET_ALL)
        except ValueError:
            # Handle non-integer input
            print("\n Please enter the genre number.")

    # Prompt the user to enter a release year within the allowed range
    while True:
        try:
            year = int(input(Fore.BLUE + "\n✅ Please enter the movie release year (range from 1900 to 2025): " + Style.RESET_ALL))
            if 1900 <= year <= 2025:
                break
            else:
                # Handle year outside the allowed range
                print(Fore.YELLOW + "The year must be within the range of 1900 to 2025." + Style.RESET_ALL)
        except ValueError:
            # Handle non-integer input for year
            print(Fore.YELLOW + "Please enter a valid year." + Style.RESET_ALL)

    # Perform the search based on selected genre and year
    movies = db_operations.search_movies_by_genre_and_year(genre, year)
    # Save the search query for future analytics
    db_operations.save_search_query('genre_year', f"{genre}_{year}")

    # Display the results if any movies are found
    if movies:
        display.show_movies(movies)
    else:
        display.show_no_results()

# Function to display the most popular search queries
def handle_show_popular_queries():
    # Retrieve the popular queries from the database
    queries = db_operations.get_popular_queries()
    if queries:
        # Display the popular queries
        display.show_popular_queries(queries)
    else:
        # Show a "no results" message if no queries are found
        display.show_no_results()
