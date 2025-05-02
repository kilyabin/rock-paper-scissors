
# Dictionary containing ASCII art for Rock, Paper, and Scissors.
# Keys are the base (Russian) names of the moves.
ascii_art = {
    "камень": [
        "    _______",
        "---'   ____)",
        "      (_____) ",
        "      (_____) ",
        "      (____)",
        "---.__(___) "
    ],
    "бумага": [
        "    _______",
        "---'   ____)____",
        "          ______)",
        "          _______)",
        "         _______)",
        "---.__________) "
    ],
    "ножницы": [
        "    _______",
        "---'   ____)____",
        "          ______)",
        "       __________) ",
        "      (____)",
        "---.__(___) "
    ]
}

def get_ascii_art(move_name):
    """
    Retrieves the ASCII art for a given move name.

    Args:
        move_name (str): The base name of the move ('камень', 'ножницы', 'бумага').

    Returns:
        list: A list of strings representing the ASCII art, or None if the move is not found.
    """
    return ascii_art.get(move_name)

def display_ascii_art_side_by_side(player_move_art, computer_move_art):
    """
    Displays the ASCII art for player and computer moves side by side.

    Args:
        player_move_art (list): List of strings for player's ASCII art.
        computer_move_art (list): List of strings for computer's ASCII art.
    """
    if not player_move_art or not computer_move_art:
        print("Error: Could not display ASCII art.")
        return

    # Ensure both arts have the same number of lines (pad with empty lines if needed)
    max_lines = max(len(player_move_art), len(computer_move_art))
    player_move_art += [""] * (max_lines - len(player_move_art))
    computer_move_art += [""] * (max_lines - len(computer_move_art))

    # Headers (adjust spacing as needed)
    # The spacing here is an estimate and might need adjustment based on the actual terminal width and art size.
    header_spacing = 20 # Initial guess for spacing
    print("Игрок:" + " " * header_spacing + "Компьютер:")

    for i in range(max_lines):
        # Pad lines to ensure alignment
        # Adjust padding based on the expected maximum width of a single art piece
        line_padding = 20 # Adjust padding based on art width
        player_line = player_move_art[i].ljust(line_padding)
        computer_line = computer_move_art[i]
        print(f"{player_line}{computer_line}")

