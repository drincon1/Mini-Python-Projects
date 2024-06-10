def main():
    print("Welcome to Mastermind Game!")
    first()
    

def first():
    number = input("Player 1, please enter the number: ")
    secret = 'X'*len(number)
    won = False
    tries = 0
    first_try = True
    mastermind = False
    while not won and not mastermind:
        index = secret.find('X')
        if index != -1:
            guess = input("Player 2, enter your guess: ")
            tries += 1
            if first_try and number == guess:
                mastermind = True
                print("You got it on the first try! You are the Mastermind!")
            first_try = False
            correct = 0
            for i in range(0, len(guess)):
                post = number.find(guess[i])
                if post != -1:
                    correct += 1
                    secret = secret[:post] + number[post] + secret[post+1:]
                    
            print(f"You got {correct} correct numbers\n{secret}")
        else: 
            print(f"You guessed the number! {number} in {tries} tries")
            won = True
    
    if not mastermind:
        second(tries)    

def second(tries):
    number = input("Player 2, please enter the number: ")
    secret = 'X'*len(number)
    won = False
    tries1 = 0
    
    while not won:
        index = secret.find('X')
        if index != -1:
            guess = input("Player 1, enter your guess: ")
            tries1 += 1
            correct = 0
            for i in range(0, len(guess)):
                post = number.find(guess[i])
                if post != -1:
                    correct += 1
                    secret = secret[:post] + number[post] + secret[post+1:]
                    
            print(f"You got {correct} correct numbers\n{secret}")
        else: 
            print(f"You guessed the number! {number} in {tries1} tries")
            won = True
    
    if tries < tries1:
        print("Player 2 is the Mastermind! Congratulations!")
    elif tries == tries1:
        print("It was a tie!")
    else:
        print("Player 1 is the Mastermind! Congratulations!")
        
if __name__ == '__main__':
    main()