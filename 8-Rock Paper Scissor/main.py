import random

def main():
    print("Rock Paper Scissor...who will win?")

    choice = input("\nRock Paper Scissor\nIf you wan to stop enter 'q'\n")
    comp_wins = 0
    wins = 0
    
    while choice != "q":
        choices = ["Rock", "Paper", "Scissor"]
        choices.remove(choice)
        
        comp_choice = choices[random.randint(0,1)]
        print(f"The result was: {choice} vs {comp_choice}")
        if choice == "Rock" and comp_choice == "Scissor":
            print("You won!")
            wins += 1
        elif choice == "Paper" and comp_choice == "Rock":
            print("You won!")
            wins += 1
        elif choice == "Scissor" and comp_choice == "Paper":
            print("You won!")
            wins += 1
        else:
            print("You loss")
            comp_wins += 1
        choice = input("\nRock Paper Scissor\nIf you wan to stop enter 'q'\n")
    
    if comp_wins < wins:
        print(f"You won! {wins} vs {comp_wins}")
    elif comp_wins > wins:
        print(f"You lost! {wins} vs {comp_wins}")
    else:
        print(f"Draw! {wins} vs {comp_wins}")

if __name__ == '__main__':
    main()