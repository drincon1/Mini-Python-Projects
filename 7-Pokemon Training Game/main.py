def main():
    print("Welcome to Pokemon Training")

    powers = []
    looking = True
    mini, maxi = 0,0
    while looking:
        pokemon = input("Please enter the powers of the new pokemon (Note: Min, Max)\nIf you stoped looking type 'q'\n")
        if pokemon != "q":
            pokemon = pokemon.split(",")
    
            if len(powers) == 0:
                mini = int(pokemon[0])
                maxi = int(pokemon[1])
            else:
                mini = min(mini,int(pokemon[0]))
                maxi = max(maxi,int(pokemon[1]))
                
            powers.append(int(pokemon[0]))
            powers.append(int(pokemon[1]))
            
        else:
            looking = False
        print(f"\nThe available powers are: {powers}")
        print(f"Min: {mini}, Max: {maxi}\n")    

if __name__ == "__main__":
    main()