#author: Madeleine Elias
#date: 4/17/26
#description: user plays battleship against computer
#each ~ is a boat, x is hit, o is miss 🚢
import random
hitboard = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] #where player is shooting towards
board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] #where your boats are 
computerboats = []
personboats=[]
pwin = []
cwin = []
def print_board(board):
    '''description: prints the board. One is where player is shooting, other is the one with your boats
    args: 
        board: either the players board or the computers
    returns: prints the boards'''
    print("")
    print(f'| {board[0]} | {board[1]} | {board[2]} | {board[3]} | {board[4]} |')
    print(f'| {board[5]} | {board[6]} | {board[7]} | {board[8]} | {board[9]}|')
    print(f'| {board[10]}| {board[11]}| {board[12]}| {board[13]}| {board[14]}|')
    print(f'| {board[15]}| {board[16]}| {board[17]}| {board[18]}| {board[19]}|')
    print(f'| {board[20]}| {board[21]}| {board[22]}| {board[23]}| {board[24]}|')
    print("")

def c_pickb():
    '''Description: picks where the boats are for the computer randomly
    args: none
    returns: adds the move to a list to keep track of them'''
    for _ in range(4):
        while True:
            move = random.randint(1,25)
            if move not in computerboats:
                computerboats.append(move)
                break  
def p_pickb():
    '''description: the player picks where the boats are
    args: none
    returns: adds the boats to a list to keep track and puts a ship (~) on the board'''
    for _ in range(4):
        while True:
            copy = 0
            mv = input("where would you like to place a boat ")
            if mv=="1"or mv=="2"or mv=="3"or mv=="4"or mv=="5"or mv=="6"or mv=="7"or mv=="8"or mv=="9"or mv=="10"or mv=="11"or mv=="12"or mv=="13"or mv=="14"or mv=="15"or mv=="16"or mv=="17"or mv=="18"or mv=="19"or mv=="20"or mv=="21"or mv=="22"or mv=="23"or mv=="24"or mv=="25":
                copy = copy+1
                mv = int(mv)
                if mv not in personboats:
                    copy = copy+1
            if copy == 2:
                break
        personboats.append(mv)
        if (mv-1)<10:
            board[(mv-1)]="~"
        else:
            board[(mv-1)]="~ "

def person_move():
    '''description: the player picks where to make a shot
    args: none
    returns: shoots other board if its a hit x if it misses o'''
    while True:
        copy = 0 
        mv = input("where would you like to hit ")
        if mv=="1"or mv=="2"or mv=="3"or mv=="4"or mv=="5"or mv=="6"or mv=="7"or mv=="8"or mv=="9"or mv=="10"or mv=="11"or mv=="12"or mv=="13"or mv=="14"or mv=="15"or mv=="16"or mv=="17"or mv=="18"or mv=="19"or mv=="20"or mv=="21"or mv=="22"or mv=="23"or mv=="24"or mv=="25":
            copy = copy+1
            mv = int(mv)
            mv = mv -1
            if hitboard[mv]!="o" and hitboard[mv]!="x" and hitboard[mv]!="x " and hitboard[mv]!="o ": 
                copy = copy+1
                mv = mv +1
        if copy == 2:
            break
    if mv in computerboats:
        pwin.append(1)
        if (mv-1)<10:
            hitboard[(mv-1)]="x"
        else:
            hitboard[(mv-1)]="x "
        print("you hit them")
    else:
        if (mv-1)<10:
            hitboard[(mv-1)]="o"
        else:
            hitboard[(mv-1)]="o "
        print("you missed them")
def computer_move():
    '''decription: computer randomly chooses where to hit
    args: none
    returns: puts an x on player board if it hits, an o if misses'''
    while True:
        move = random.randint(0,24)
        if board[move]!="x" and board[move]!="o" and board[move]!="o " and board[move]!="x ":
            break
    if (move+1) in personboats:
        cwin.append(1)
        if move <10:
            board[move]="x"
        else:
            board[move]="x "
        print("you got hit")
    else:
        if move<10:
            board[move]="o"
        else:
            board[move]="o "
        print("the computer missed")

def win():
    '''description: checks to see if there is a winner yet
    args: none
    returns: win if there is a win'''
    if len(pwin) == 4:
        print("player wins")
        return "win"
    if len(cwin) == 4:
        print("computer wins")
        return "win"
def clearboard():
    '''description: clears the board so they can play again
    args: none
    returns: changes all the varibles to what they originally where'''
    hitboard[:] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] #where player is shooting towards
    board[:] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] #where your boats are 
    computerboats[:] = []
    personboats[:]=[]
    pwin[:] = []
    cwin[:] = []

def main():
    while True:
        question = input("do you want to play? y/n ").lower()
        if question == "n":
            exit()
        if question == "y":
            print_board(board)
            c_pickb()
            p_pickb()
            print_board(board)
            while True:
                person_move()
                print_board(hitboard)
                print_board(board)
                wins = win()
                if wins == "win":
                    clearboard()
                    break
                computer_move()
                print_board(hitboard)
                print_board(board)
                wins = win()
                if wins == "win":
                    clearboard
                    break
main()