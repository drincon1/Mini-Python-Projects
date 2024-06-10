import random

def main():
    print("Welcoe to 2048! Lets have some fun")
    mat = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]        
    ]
    
    # row = random.randint(0,3)
    # col = random.randint(0,3)
    # mat[row][col] = 2
    game(mat)



def game(mat):
    won = False
    spaces = 1 # number of spaces that already have a number
    game_over = False
    while not game_over and not won and spaces < 16:
        printMat(mat)
        move = input("a: Left\nd: Right\nw: Up\nd: sown\nq: Quit\n")
        
        if move == "a":
            for i in range(0,4):
                mat = moveLeft(mat,i,3)
                mat, change = sumLeft(mat,i)
                if change:
                    moveLeft(mat,i,3)
                    
        elif move == "d":
            for i in range(0,4):
                mat =  moveRight(mat,i,0)
                mat, change = sumRight(mat,i)
                if change:
                    mat = moveRight(mat,i,0)
                    
        elif move == "w":
            for j in range(0,4):
                mat = moveUp(mat,3,j)
                mat, change = sumUp(mat,j)
                if change:
                    mat = moveUp(mat,3,j)
            
        elif move == "s":
            for j in range(0,4):
                mat = moveDown(mat,0,j)
                mat, change = sumDown(mat,j)
                if change:
                    mat = moveDown(mat,0,j)
                
        elif move == "q":
            game_over = True
        else:
            print("Invalid input")
        
        if not checkWin(mat):
            mat = newRandom(mat)
            spaces = countZeros(mat)
        else:
            won = True
    
    if won:
        print("Congratulations! You won!")
        printMat(mat)
    else:
        print("GAME OVER")
        printMat(mat)
        
            
def moveLeft(mat,i,j):
    if j == 0:
        return mat
    if mat[i][j] == 0:
        mat = moveLeft(mat,i,j-1)
    if mat[i][j-1] != 0:
        mat = moveLeft(mat,i,j-1)
    if mat[i][j-1] == 0:
        mat[i][j-1] = mat[i][j]
        mat = moveLeft(mat,i,j-1)
        mat[i][j] = 0
    
    return mat

def sumLeft(mat,i):
    change = False
    for j in range (0,3):
        if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
            mat[i][j] = mat[i][j] + mat[i][j+1]
            mat[i][j+1] = 0
            change = True
    
    return mat, change


def moveRight(mat,i,j):
    if j == 3:
        return mat
    if mat[i][j] == 0:
        mat = moveRight(mat,i,j+1)
    if mat[i][j+1] != 0:
        mat = moveRight(mat,i,j+1)
    if mat[i][j+1] == 0:
        mat[i][j+1] = mat[i][j]
        mat = moveRight(mat,i,j+1)
        mat[i][j] = 0
        
    return mat

def sumRight(mat,i):
    change = False
    for j in range (3,0,-1):
        if mat[i][j] != 0 and mat[i][j] == mat[i][j-1]:
            mat[i][j] = mat[i][j] + mat[i][j-1]
            mat[i][j-1] = 0
            change = True
    
    return mat, change

def moveUp(mat,i,j):
    if i == 0:
        return mat
    if mat[i][j] == 0:
        mat = moveUp(mat,i-1,j)
    if mat[i-1][j] != 0:
        mat = moveUp(mat,i-1,j)
    if mat[i-1][j] == 0:
        mat[i-1][j] = mat[i][j]
        mat = moveUp(mat,i-1,j)
        mat[i][j] = 0
        
    return mat

def sumUp(mat,j):
    change = False
    for i in range (0,3):
        if mat[i][j] != 0 and mat[i][j] == mat[i+1][j]:
            mat[i][j] = mat[i][j] + mat[i+1][j]
            mat[i+1][j] = 0
            change = True
    
    return mat, change

def moveDown(mat,i,j):
    if i == 3:
        return mat
    if mat[i][j] == 0:
        mat = moveDown(mat,i+1,j)
    if mat[i+1][j] != 0:
        mat = moveDown(mat,i+1,j)
    if mat[i+1][j] == 0:
        mat[i+1][j] = mat[i][j]
        mat = moveDown(mat,i+1,j)
        mat[i][j] = 0
        
    return mat

def sumDown(mat,j):
    change = False
    for i in range (3,0,-1):
        if mat[i][j] != 0 and mat[i][j] == mat[i-1][j]:
            mat[i][j] = mat[i][j] + mat[i-1][j]
            mat[i-1][j] = 0
            change = True
    
    return mat, change


def checkWin(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return True
    return False

def countZeros(mat):
    counter = 0
    for i in range(4):
        for j in range(4):
            if mat[i][j] != 0:
                counter +=1   
    return counter

def newRandom(mat):
    set_random = False
    while not set_random:
        row = random.randint(0,3)
        col = random.randint(0,3)
        if mat[row][col] == 0:
            mat[row][col] = 2
            set_random = True
        
    return mat     

def newMat():
    mat = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]        
    ]
    return mat


def printMat(mat):
    row = ""
    for i in range(4):
        row = "[ "
        for j in range(4):
            row = row + str(mat[i][j]) + " "
        row = row + "]"
        print(row)
            
    


if __name__ == '__main__':
    main()