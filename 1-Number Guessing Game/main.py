

import random, math

def main():
    min = int(input("Minimum range: "))
    max = int(input("Maximun range: "))
    
    while min > max or max < min or min == max:
        if min > max or max < min:
            print("Ups! Wrong input! Make sure the number orders are correct")
        if min == max:
            print("Ups! The numbers can't be the same")
        min = int(input("Minimum range: "))
        max = int(input("Maximun range: "))
    
    num = random.randint(min,max)
    guess = num + 1
    counter = 0
    min_count = int(math.log2(max-min+1))
    
    while guess != num:
        guess = int(input("Guess the number\n"))
        counter += 1
        if guess != num:
            if guess > num:
                print("You guess to high")
            else:
                print("You guess to little")
    
    if counter < min_count:
        print(f"Great! You guessed in {counter} tries!\n{min_count} was the minimun amount")
    else:
        print(f"Ups! The minimun amount of guess were {min_count}.\nYou guessed in {counter}")
            
        

if __name__ == "__main__":
    main()
    