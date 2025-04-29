from prettytable import PrettyTable
from colorama import Fore, Style

# Function to display a list of movies in a formatted table
def show_movies(movies):
    table = PrettyTable()
    table.field_names = ["Title", "Release year", "Description"] # Set the table headers
    for title, year, description in movies:
        table.add_row([title, year, description]) # Add each movie as a new row
    print(Fore.GREEN + "\nSearch results:" + Style.RESET_ALL)
    print(table)

# Function to display the top 10 most popular search queries in a table
def show_popular_queries(queries):
    table = PrettyTable()
    table.field_names = ["Search type", "Search text", "Quantity"] # Set the table headers
    for search_type, search_text, search_count in queries:
        table.add_row([search_type, search_text, search_count]) # Add each query as a new row
    print(Fore.CYAN + "\n📊Top 10 the most pupal queries:" + Style.RESET_ALL)
    print(table)

# Function to show a message if no search results were found
def show_no_results():
    print(Fore.YELLOW + "Nothing is found." + Style.RESET_ALL)

# Function to display an error message for invalid input
def show_invalid_input(message):
    print(Fore.RED + f"\nError: {message}" + Style.RESET_ALL)

# Function to display the main menu options
def show_main_menu():
    print(Fore.BLUE + "\n✅ Please select the option:" + Style.RESET_ALL)
    print("1. Search movie by keyword")
    print("2. Search movie by genre and year")
    print("3. Show 10 the most popular queries")
    print("4. Exit")
