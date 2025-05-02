import random
import ascii_art # Import the new file

# Dictionary to hold text strings for different languages
texts = {
    "ru": {
        "welcome": "Добро пожаловать в игру Камень, Ножницы, Бумага!",
        "main_menu_title": "--- Главное меню ---",
        "main_menu_play": "1 - Начать новую игру",
        "main_menu_language": "2 - Выбрать язык",
        "main_menu_exit": "3 - Выйти из игры",
        "main_menu_prompt": "Введите номер пункта меню: ",
        "invalid_menu_input": "Неверный ввод. Пожалуйста, введите 1, 2 или 3.",
        "exit_game": "Выход из игры. До свидания!",
        "start_game": "\n--- Начинаем игру ---",
        "choose_move": "Выберите ваш ход:",
        "move_rock": "1 - Камень",
        "move_scissors": "2 - Ножницы",
        "move_paper": "3 - Бумага",
        "move_back_to_menu": "0 - Вернуться в главное меню",
        "move_prompt": "Введите номер вашего выбора: ",
        "invalid_move_input": "Неверный ввод. Пожалуйста, введите 1, 2, 3 или 0.",
        "returning_to_menu": "Возвращаемся в главное меню...",
        "computer_chose": "Компьютер выбрал: {}",
        "tie": "Ничья!",
        "player_wins_round": "Вы выиграли раунд!",
        "computer_wins_round": "Компьютер выиграл раунд!",
        "score": "Счет: Игрок {} - Компьютер {}",
        "invalid_integer_input": "Неверный ввод. Пожалуйста, введите целое число.",
        "error_occurred": "Произошла ошибка: {}",
        "language_menu_title": "\n--- Выбор языка ---",
        "language_menu_russian": "1 - Русский",
        "language_menu_english": "2 - English",
        "language_menu_back": "0 - Назад в главное меню",
        "language_menu_prompt": "Выберите язык: ",
        "language_set_russian": "Язык установлен на Русский.",
        "language_set_english": "Language set to English.",
        "invalid_language_input": "Неверный ввод. Пожалуйста, введите 1, 2 или 0."
    },
    "en": {
        "welcome": "Welcome to the Rock, Paper, Scissors Game!",
        "main_menu_title": "--- Main Menu ---",
        "main_menu_play": "1 - Start New Game",
        "main_menu_language": "2 - Select Language",
        "main_menu_exit": "3 - Exit Game",
        "main_menu_prompt": "Enter menu item number: ",
        "invalid_menu_input": "Invalid input. Please enter 1, 2 or 3.",
        "exit_game": "Exiting game. Goodbye!",
        "start_game": "\n--- Starting Game ---",
        "choose_move": "Choose your move:",
        "move_rock": "1 - Rock",
        "move_scissors": "2 - Scissors",
        "move_paper": "3 - Paper",
        "move_back_to_menu": "0 - Back to Main Menu",
        "move_prompt": "Enter the number of your choice: ",
        "invalid_move_input": "Invalid input. Please enter 1, 2, 3 or 0.",
        "returning_to_menu": "Returning to main menu...",
        "computer_chose": "Computer chose: {}",
        "tie": "Tie!",
        "player_wins_round": "You won the round!",
        "computer_wins_round": "Computer won the round!",
        "score": "Score: Player {} - Computer {}",
        "invalid_integer_input": "Invalid input. Please enter an integer.",
        "error_occurred": "An error occurred: {}",
        "language_menu_title": "\n--- Language Selection ---",
        "language_menu_russian": "1 - Русский",
        "language_menu_english": "2 - English",
        "language_menu_back": "0 - Back to Main Menu",
        "language_menu_prompt": "Select language: ",
        "language_set_russian": "Язык установлен на Русский.",
        "language_set_english": "Language set to English.",
        "invalid_language_input": "Invalid input. Please enter 1, 2 or 0."
    }
}

# Default language
current_language = "ru"

def get_text(key):
    """Helper function to get text in the current language."""
    return texts[current_language].get(key, key) # Return key itself if not found

def get_player_choice_from_number(choice_number):
    """
    Converts the number choice to its string representation (in the current language).
    1 -> rock/камень
    2 -> scissors/ножницы
    3 -> paper/бумага
    """
    if choice_number == 1:
        return "камень" if current_language == "ru" else "rock"
    elif choice_number == 2:
        return "ножницы" if current_language == "ru" else "scissors"
    elif choice_number == 3:
        return "бумага" if current_language == "ru" else "paper"
    else:
        return None # Invalid number

def get_base_move_name(localized_move_name):
    """
    Converts a localized move name back to its base (Russian) name for ASCII art lookup.
    """
    if localized_move_name in ["камень", "rock"]:
        return "камень"
    elif localized_move_name in ["ножницы", "scissors"]:
        return "ножницы"
    elif localized_move_name in ["бумага", "paper"]:
        return "бумага"
    return None


def play_game():
    """
    Logic for a single round of the Rock, Paper, Scissors game.
    """
    # Use language-specific choices for comparison
    choices = ["камень", "ножницы", "бумага"] if current_language == "ru" else ["rock", "scissors", "paper"]

    player_score = 0
    computer_score = 0

    print(get_text("start_game"))

    while True:
        # Display the number-choice mapping before each turn
        print(get_text("choose_move"))
        print(get_text("move_rock"))
        print(get_text("move_scissors"))
        print(get_text("move_paper"))
        print(get_text("move_back_to_menu"))

        try:
            # Get player input as a number
            player_input = int(input(get_text("move_prompt")))

            # Check if player wants to return to main menu
            if player_input == 0:
                print(get_text("returning_to_menu"))
                return # Exit the play_game function

            # Get player choice string from the number (localized)
            player_choice_str = get_player_choice_from_number(player_input)

            # Validate player input number
            if player_choice_str is None:
                print(get_text("invalid_move_input"))
                continue # Ask for input again

            # Get computer choice (always from the base list for logic comparison)
            computer_choice_base = random.choice(["камень", "ножницы", "бумага"])

            # Get the computer choice string in the current language for display
            computer_choice_str = get_player_choice_from_number(["камень", "ножницы", "бумага"].index(computer_choice_base) + 1)

            print(get_text("computer_chose").format(computer_choice_str))

            # --- Display ASCII Art ---
            # Get the base move names for ASCII art lookup
            player_base_move = get_base_move_name(player_choice_str)
            computer_base_move = computer_choice_base # Computer choice is already base

            player_art = ascii_art.get_ascii_art(player_base_move)
            computer_art = ascii_art.get_ascii_art(computer_base_move)

            if player_art and computer_art:
                ascii_art.display_ascii_art_side_by_side(player_art, computer_art)
            else:
                print("Could not retrieve ASCII art.") # Fallback message

            # --- End Display ASCII Art ---


            # Determine the winner using the base (language-agnostic) choices for logic
            # We need the base player choice for comparison
            player_choice_base = get_base_move_name(player_choice_str)

            if player_choice_base == computer_choice_base:
                print(get_text("tie"))
            elif (player_choice_base == "камень" and computer_choice_base == "ножницы") or \
                 (player_choice_base == "ножницы" and computer_choice_base == "бумага") or \
                 (player_choice_base == "бумага" and computer_choice_base == "камень"):
                print(get_text("player_wins_round"))
                player_score += 1
            else:
                print(get_text("computer_wins_round"))
                computer_score += 1

            # Display current score
            print(get_text("score").format(player_score, computer_score))
            print() # Add an empty line for better readability

        except ValueError:
            # Handle non-integer input
            print(get_text("invalid_integer_input"))
        except Exception as e:
            print(get_text("error_occurred").format(e))


def language_menu():
    """
    Menu for selecting the game language.
    """
    global current_language # Declare that we are modifying the global variable

    while True:
        print(get_text("language_menu_title"))
        print(get_text("language_menu_russian"))
        print(get_text("language_menu_english"))
        print(get_text("language_menu_back"))

        try:
            menu_choice = int(input(get_text("language_menu_prompt")))

            if menu_choice == 1:
                current_language = "ru"
                print(get_text("language_set_russian"))
            elif menu_choice == 2:
                current_language = "en"
                print(get_text("language_set_english"))
            elif menu_choice == 0:
                print(get_text("returning_to_menu"))
                break # Exit language menu
            else:
                print(get_text("invalid_language_input"))

        except ValueError:
            print(get_text("invalid_integer_input"))
        except Exception as e:
            print(get_text("error_occurred").format(e))


def main_menu():
    """
    Main menu of the game.
    """
    print(get_text("welcome"))

    while True:
        print(get_text("main_menu_title"))
        print(get_text("main_menu_play"))
        print(get_text("main_menu_language"))
        print(get_text("main_menu_exit"))

        try:
            menu_choice = int(input(get_text("main_menu_prompt")))

            if menu_choice == 1:
                play_game() # Start the game
            elif menu_choice == 2:
                language_menu() # Go to language selection
            elif menu_choice == 3:
                print(get_text("exit_game"))
                break # Exit the main menu loop
            else:
                print(get_text("invalid_menu_input"))
        except ValueError:
            print(get_text("invalid_integer_input"))
        except Exception as e:
            print(get_text("error_occurred").format(e))

# Start the main menu when the script runs
if __name__ == "__main__":
    main_menu()
