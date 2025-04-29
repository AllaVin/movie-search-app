# Основной цикл работы программы: вывод меню, ожидание команд от пользователя, вызов обработчика команд.

import command_handler
from colorama import init, Fore, Style
import display

init(autoreset=True)


def main():
    print(Fore.BLUE + "\n---=== 🎥 Welcome to the Movie Search application! ===---" + Style.RESET_ALL)
    while True:
        display.show_main_menu()
        choice = input(Fore.BLUE + "\n✅ Enter the number of option: " + Style.RESET_ALL)

        try:
            if choice == "1":
                command_handler.handle_search_by_keyword()
            elif choice == "2":
                command_handler.handle_search_by_genre_and_year()
            elif choice == "3":
                command_handler.handle_show_popular_queries()
            elif choice == "4":
                print(Fore.YELLOW + "\n🙌 Closing the application. See you later!" + Style.RESET_ALL)

                break
            else:
                display.show_invalid_input("Incorrect number of the option is entered.")
        except Exception as e:
            display.show_invalid_input(f"Something went wrong: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n🛑 The program was stopped by the user. Goodbye!" + Style.RESET_ALL)
