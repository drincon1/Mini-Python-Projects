import random

def main():
    print("Welcome to Cows and Bulls! Lets guess some numbers!")
    guessed = False
    
    counter = 0
    numbers = []
    code = ""
    
    while counter < 4:
        ran = random.randint(0,9)
        if ran not in numbers:
            numbers.append(ran)
            code = code + str(ran)
            counter += 1
    
    # print(f"The code is: {code}")
    
    while not guessed:
        guess = input("Guess the code (It's only four digits)\n")
        if len(guess) == 4:
            if guess != code:
                cows = 0
                bulls = 0
                
                for i in range(0,len(code)):
                    if code[i] == guess[i]:
                        bulls += 1
                    elif guess[i] in code:
                        cows += 1
                
                
                print(f"\n***\nBulls: {bulls}\nCows: {cows}\n***\n")
            else:
                guessed = True
                print("You cracked the code! Congratulations")
        
        

if __name__ == '__main__':
    main()