# import random

# # Constants for the game
# BOARD_SIZE = 10
# SHIPS = {
#     'Carrier': 5,
#     'Battleship': 4,
#     'Destroyer': 3,
#     'Submarine': 3,
#     'Patrol Boat': 2
# }
# HIT = 'X'
# MISS = 'O'
# EMPTY = '-'

# # Initialize the game board
# def initialize_board():
#     return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# # Print the game board
# def print_board(board, reveal=False):
#     for row in board:
#         if reveal:
#             print(' '.join(row))
#         else:
#             print(' '.join([cell if cell in (HIT, MISS) else EMPTY for cell in row]))
#     print()

# # Check if the ship can be placed on the board
# def can_place_ship(board, ship_size, x, y, orientation):
#     if orientation == 'H':
#         if y + ship_size > BOARD_SIZE:
#             return False
#         return all(board[x][y + i] == EMPTY for i in range(ship_size))
#     else:  # orientation == 'V'
#         if x + ship_size > BOARD_SIZE:
#             return False
#         return all(board[x + i][y] == EMPTY for i in range(ship_size))

# # Place ships randomly on the board
# def place_ships(board):
#     ships = {}
#     for ship, size in SHIPS.items():
#         placed = False
#         while not placed:
#             x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
#             orientation = random.choice(['H', 'V'])
#             if can_place_ship(board, size, x, y, orientation):
#                 if orientation == 'H':
#                     for i in range(size):
#                         board[x][y + i] = ship[0]
#                 else:  # orientation == 'V'
#                     for i in range(size):
#                         board[x + i][y] = ship[0]
#                 ships[ship] = (x, y, orientation, size)
#                 placed = True
#     return ships

# # Get user input for the guess
# def get_user_guess():
#     while True:
#         try:
#             x = int(input("Enter row (0-9): "))
#             y = int(input("Enter column (0-9): "))
#             if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
#                 return x, y
#             else:
#                 print("Invalid input. Please enter numbers between 0 and 9.")
#         except ValueError:
#             print("Invalid input. Please enter valid numbers.")

# # Get AI guess
# def get_ai_guess(guesses):
#     while True:
#         x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
#         if (x, y) not in guesses:
#             return x, y

# # Check the guess
# def check_guess(board, ships, guess):
#     x, y = guess
#     if board[x][y] == HIT or board[x][y] == MISS:
#         return False
#     for ship, (sx, sy, orientation, size) in ships.items():
#         if orientation == 'H' and sx == x and sy <= y < sy + size:
#             board[x][y] = HIT
#             print(f"Hit! {'User' if guesses == user_guesses else 'AI'} hit the {ship}.")
#             return True
#         elif orientation == 'V' and sy == y and sx <= x < sx + size:
#             board[x][y] = HIT
#             print(f"Hit! {'User' if guesses == user_guesses else 'AI'} hit the {ship}.")
#             return True
#     board[x][y] = MISS
#     print("Miss!")
#     return False

# # Main game loop
# def play_game():
#     user_board = initialize_board()
#     ai_board = initialize_board()
#     user_ships = place_ships(user_board)
#     ai_ships = place_ships(ai_board)
    
#     print("Let's play Battleship!")
#     print("User's board:")
#     print_board(user_board, reveal=True)
#     print("AI's board:")
#     print_board(ai_board)  # Print an empty board for the user

#     total_ship_cells = sum(SHIPS.values())
#     user_hits = 0
#     ai_hits = 0
#     user_guesses = []
#     ai_guesses = []

#     while user_hits < total_ship_cells and ai_hits < total_ship_cells:
#         print("Your turn!")
#         user_guess = get_user_guess()
#         user_guesses.append(user_guess)
#         if check_guess(ai_board, ai_ships, user_guess):
#             user_hits += 1
#         print_board(ai_board)

#         print("AI's turn!")
#         ai_guess = get_ai_guess(ai_guesses)
#         ai_guesses.append(ai_guess)
#         if check_guess(user_board, user_ships, ai_guess):
#             ai_hits += 1
#         print_board(user_board, reveal=True)

#     if user_hits == total_ship_cells:
#         print("Congratulations! You sank all the AI's ships!")
#     else:
#         print("Sorry, the AI sank all your ships. Better luck next time!")

# # Start the game
# if __name__ == "__main__":
#     play_game()


import random

# Constants for the game
BOARD_SIZE = 10
SHIPS = {
    'Carrier': 5,
    'Battleship': 4,
    'Destroyer': 3,
    'Submarine': 3,
    'Patrol Boat': 2
}
HIT = 'X'
MISS = 'O'
EMPTY = '-'

# Initialize the game board
def initialize_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Print the game board
def print_board(board, reveal=False):
    for row in board:
        if reveal:
            print(' '.join(row))
        else:
            print(' '.join([cell if cell in (HIT, MISS) else EMPTY for cell in row]))
    print()

# Check if the ship can be placed on the board
def can_place_ship(board, ship_size, x, y, orientation):
    if orientation == 'H':
        if y + ship_size > BOARD_SIZE:
            return False
        return all(board[x][y + i] == EMPTY for i in range(ship_size))
    else:  # orientation == 'V'
        if x + ship_size > BOARD_SIZE:
            return False
        return all(board[x + i][y] == EMPTY for i in range(ship_size))

# Place ships randomly on the board
def place_ships(board):
    ships = {}
    for ship, size in SHIPS.items():
        placed = False
        while not placed:
            x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
            orientation = random.choice(['H', 'V'])
            if can_place_ship(board, size, x, y, orientation):
                if orientation == 'H':
                    for i in range(size):
                        board[x][y + i] = ship[0]
                else:  # orientation == 'V'
                    for i in range(size):
                        board[x + i][y] = ship[0]
                ships[ship] = (x, y, orientation, size)
                placed = True
    return ships

# Get user input for the guess
def get_user_guess():
    while True:
        try:
            x = int(input("Enter row (0-9): "))
            y = int(input("Enter column (0-9): "))
            if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                return x, y
            else:
                print("Invalid input. Please enter numbers between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Get AI guess
def get_ai_guess():
    return random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)

# Check the guess
def check_guess(board, ships, guess):
    x, y = guess
    if board[x][y] == HIT or board[x][y] == MISS:
        return False
    for ship, (sx, sy, orientation, size) in ships.items():
        if orientation == 'H' and sx == x and sy <= y < sy + size:
            board[x][y] = HIT
            print(f"Hit! You hit the {ship}.")
            return True
        elif orientation == 'V' and sy == y and sx <= x < sx + size:
            board[x][y] = HIT
            print(f"Hit! You hit the {ship}.")
            return True
    board[x][y] = MISS
    print("Miss!")
    return False

# Main game loop
def play_game():
    user_board = initialize_board()
    ai_board = initialize_board()
    user_ships = place_ships(user_board)
    ai_ships = place_ships(ai_board)
    
    print("Let's play Battleship!")
    print("User's board:")
    print_board(user_board, reveal=True)
    print("AI's board:")
    print_board(ai_board)  # Print an empty board for the user

    total_ship_cells = sum(SHIPS.values())
    user_hits = 0
    ai_hits = 0

    while user_hits < total_ship_cells and ai_hits < total_ship_cells:
        print("Your turn!")
        user_guess = get_user_guess()
        if check_guess(ai_board, ai_ships, user_guess):
            user_hits += 1
        print_board(ai_board)

        print("AI's turn!")
        ai_guess = get_ai_guess()
        if check_guess(user_board, user_ships, ai_guess):
            ai_hits += 1
        print_board(user_board, reveal=True)

    if user_hits == total_ship_cells:
        print("Congratulations! You sank all the AI's ships!")
    else:
        print("Sorry, the AI sank all your ships. Better luck next time!")

# Start the game
if __name__ == "__main__":
    play_game()
