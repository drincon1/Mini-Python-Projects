def main():
    print("Welcome to FLAMES! Lets see your future")
    first = input("First name: ")
    second = input("Second name: ")
    
    temp_first = list(first)
    temp_second = list(second)
    
    for x in first:
        if x in temp_second:
            temp_first.remove(x)
            temp_second.remove(x)
    
    print(f"The remaining names were:\n{temp_first}\n{temp_second}")
    letters = len(temp_first) + len(temp_second)
    print(f"The remaining amount of letters is: {letters}")
    
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    index = 0
    while len(flames) > 1:
        amount = len(flames)
        counter = 1
        
        if index >= amount:
            index = 0
            
        while counter < letters:
            index += 1
            if index >= amount:
                index = 0
            counter += 1
        flames.pop(index)
    
    print(f"The result is: {flames}")
            
            
            
            
        
        


if __name__ == '__main__':
    main()