import random

def main():
    first = input("Who is the first player?\n")
    second = input("Who is the second player?\n")
    
    ran = random.randint(1,2)
    if ran == 1:
        print(f"{first} You will go first")
        game(first,second)
    else:
        print(f"{second} You will go first")
        game(second,first)


def game(first, second):
    numbers = []
    last = False
    dis = False
    
    turn = True
    player = first
    
    while not last and not dis:
        turns = int(input(f"{player} How many numbers will you like to enter?\n"))
        
        for i in range(0,turns):
            if not last and not dis:
                number = int(input("Number: "))
                if number == 21 or (number==20 and i < turns-1):
                    print(f"{player} You lost!")
                    last = True
                    i = turns
                else:
                    if len(numbers) > 0 and not dis:
                        if not check(numbers,number):
                            dis = True
                            print(f"{player} You are made a mistake! You loss!")
                    if not dis:
                        numbers.append(number)
        
        if turn and not last and not dis:
            player = second
            turn = False
        elif not turn and not last and not dis:
            player = first
            turn = True

def check(numbers,number):
    return numbers[-1]+1 == number

if __name__ == '__main__':
    main()