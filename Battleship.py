#battleship
#each () is a boat
#x is hit
#o is miss
import random
hitboard = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] #where player is shooting towards
board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] #where your boats are 
computerboats = []
personboats=[]
pwin = []
cwin = []

def print_board():
    print("")
    print("")
    print(f'| {hitboard[0]}| {hitboard[1]}| {hitboard[2]}| {hitboard[3]}| {hitboard[4]}|')
    print(f'| {hitboard[5]}| {hitboard[6]}| {hitboard[7]}| {hitboard[8]}| {hitboard[9]}|')
    print(f'|{hitboard[10]}|{hitboard[11]}|{hitboard[12]}|{hitboard[13]}|{hitboard[14]}|')
    print(f'|{hitboard[15]}|{hitboard[16]}|{hitboard[17]}|{hitboard[18]}|{hitboard[19]}|')
    print(f'|{hitboard[20]}|{hitboard[21]}|{hitboard[22]}|{hitboard[23]}|{hitboard[24]}|')
    print("")
    print(f'| {board[0]}| {board[1]}| {board[2]}| {board[3]}| {board[4]}|')
    print(f'| {board[5]}| {board[6]}| {board[7]}| {board[8]}| {board[9]}|')
    print(f'|{board[10]}|{board[11]}|{board[12]}|{board[13]}|{board[14]}|')
    print(f'|{board[15]}|{board[16]}|{board[17]}|{board[18]}|{board[19]}|')
    print(f'|{board[20]}|{board[21]}|{board[22]}|{board[23]}|{board[24]}|')

def c_pickb():
    for _ in range(4):
        while True:
            move = random.randint(1,25)
            if move not in computerboats:
                computerboats.append(move)
                break
        
def p_pickb():
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
        board[(mv-1)]="()"

def person_move():
    while True:
        copy = 0 
        mv = input("where would you like to hit ")
        if mv=="1"or mv=="2"or mv=="3"or mv=="4"or mv=="5"or mv=="6"or mv=="7"or mv=="8"or mv=="9"or mv=="10"or mv=="11"or mv=="12"or mv=="13"or mv=="14"or mv=="15"or mv=="16"or mv=="17"or mv=="18"or mv=="19"or mv=="20"or mv=="21"or mv=="22"or mv=="23"or mv=="24"or mv=="25":
            copy = copy+1
            mv = int(mv)
            mv = mv -1
            if hitboard[mv]!="o" and hitboard[mv]!="x":
                copy = copy+1
                mv = mv +1
        if copy == 2:
            break
    if mv in computerboats:
        pwin.append(1)
        hitboard[(mv-1)]="x"
        print("you hit them")
    else:
        hitboard[(mv-1)]="o"
        print("you missed them")

def computer_move():
    while True:
        move = random.randint(0,24)
        if board[move]!="x" and board[move]!="o":
            break
    if (move+1) in personboats:
        cwin.append(1)
        board[move]="x"
        print("you got hit")
    else:
        board[move]="o"
        print("the computer missed")

def win():
    if len(pwin) == 4:
        print("player wins")
        exit()
    if len(cwin) == 4:
        print("computer wins")
        exit()

def main():
    print_board()
    c_pickb()
    p_pickb()
    print_board()
    while True:
        person_move()
        print_board()
        win()
        computer_move()
        print_board()
        win()
main()