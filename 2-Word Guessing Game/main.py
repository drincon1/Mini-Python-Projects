import random


def main():
    name = input("What is your name?: ")
    
    words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 
             'player', 'condition','reverse', 'water', 'board', 'geeks']

    
    word = words[random.randint(0,len(words)-1)]
    temp = "-"*len(word)
    counter = 0
    letters = []
    
    while counter < 12 and temp != word:
        counter += 1
        letter = input(f"Letters guessed: {letters}\nWord until now:{temp}\nAttempts: {counter-1}\nGive me a letter: ")
        letters.append(letter)
        indexes = []
        for i in range(0,len(word)):
            if word[i] == letter:
                indexes.append(i)
        if len(indexes) > 0:
            for ind in indexes:
                temp = temp[:ind] + letter + temp[ind+1:]
        print(temp)
    
    if temp == word:
        print(f"Congratulations {name}! You won! It took you {counter} tries!")
    else:
        print(f"Ups {name}! It took you more than 12 attempts to guess the word.\nThe correct word was {word}")
            
            
    

if __name__ == "__main__":
    main()