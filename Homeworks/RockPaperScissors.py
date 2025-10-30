import random

def show_menu():
    print("\nRock Paper Scissors Game")
    print("1. Play Game")
    print("2. Show Stats")
    print("3. Quit")

def get_player_move():
    while True:
        try:
            print("\nChoose your move:")
            print("1. Rock")
            print("2. Paper") 
            print("3. Scissors")
            move = int(input("Enter 1, 2, or 3: "))
            if move == 1 or move == 2 or move == 3:
                return move
            else:
                print("Please enter 1, 2, or 3!")
        except ValueError:
            print("Please enter a number!")

def get_computer_move():
    return random.randint(1, 3)

def move_name(move):
    if move == 1:
        return "Rock"
    elif move == 2:
        return "Paper"
    else:
        return "Scissors"

def find_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        return "player"
    else:
        return "computer"

def show_result(player, computer, winner):
    print("\nYou picked:", move_name(player))
    print("Computer picked:", move_name(computer))
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")

def show_stats(player_wins, computer_wins, ties):
    total = player_wins + computer_wins + ties
    print("\nGame Stats:")
    print("Games played:", total)
    print("You won:", player_wins)
    print("Computer won:", computer_wins)
    print("Ties:", ties)

def play_rounds():
    while True:
        try:
            rounds = int(input("\nHow many rounds? "))
            if rounds > 0:
                break
            else:
                print("Enter a number greater than 0!")
        except ValueError:
            print("Please enter a number!")
    
    player_wins = 0
    computer_wins = 0
    ties = 0
    
    # Play each round using for loop
    for round_num in range(1, rounds + 1):
        print("\nRound", round_num)
        
        player_move = get_player_move()
        computer_move = get_computer_move()
        winner = find_winner(player_move, computer_move)
        
        show_result(player_move, computer_move, winner)
        
        # Count wins
        if winner == "player":
            player_wins = player_wins + 1
        elif winner == "computer":  
            computer_wins = computer_wins + 1
        else:
            ties = ties + 1
    
    # Show final results
    print("\nFinal Results:")
    print("You won", player_wins, "rounds")
    print("Computer won", computer_wins, "rounds") 
    print("Tied", ties, "rounds")
    
    if player_wins > computer_wins:
        print("You won overall!")
    elif computer_wins > player_wins:
        print("Computer won overall!")
    else:
        print("Overall tie!")
        
    return player_wins, computer_wins, ties

def main():
    # Variables to track all games
    total_player_wins = 0
    total_computer_wins = 0
    total_ties = 0
    
    print("Welcome to Rock Paper Scissors!")
    
    # Main game loop using while loop
    while True:
        show_menu()
        
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1 or choice == 2 or choice == 3:
                    break
                else:
                    print("Please enter 1, 2, or 3!")
            except ValueError:
                print("Please enter a number!")
        
        if choice == 3:  # Quit
            print("\nThanks for playing!")
            if total_player_wins + total_computer_wins + total_ties > 0:
                show_stats(total_player_wins, total_computer_wins, total_ties)
            print("Goodbye!")
            break
            
        elif choice == 2:  # Show stats
            if total_player_wins + total_computer_wins + total_ties == 0:
                print("\nNo games played yet!")
            else:
                show_stats(total_player_wins, total_computer_wins, total_ties)
                
        elif choice == 1:  # Play game
            player_wins, computer_wins, ties = play_rounds()
            
            # Add to total scores
            total_player_wins = total_player_wins + player_wins
            total_computer_wins = total_computer_wins + computer_wins  
            total_ties = total_ties + ties

# Start the game
main()