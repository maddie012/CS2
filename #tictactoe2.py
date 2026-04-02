#Author: madeleine elias
#description: user can play tic tac toe against a computer. If user wants to play against another person go to original tic tac toe file called Tic_tac_toe.py
#sources: old tic tac toe code
#log: 2nd tic tac toe code

import random
#Computer is x
#player is o
winning_moves= [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

player_moves = []
computer_moves = []  
#these keep track of what moves the player makes in rows, columns and diagonals to know if there is only one left and if the computer has to move there
row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]
allrows = [row1, row2, row3]
column1 = [1,4,7]
column2 = [2,5,8]
column3 = [3,6,9]
allcolumns = [column1, column2, column3]
diag1 = [1,5,9]
diag2 = [3,5,7]
alldiag = [diag1,diag2]
#next ones are just for computer to keep tract they are here for the exact same reason as the others
crow1 = [1,2,3]
crow2 = [4,5,6]
crow3 = [7,8,9]
callrows = [crow1, crow2, crow3]
ccolumn1 = [1,4,7]
ccolumn2 = [2,5,8]
ccolumn3 = [3,6,9]
callcolumns = [ccolumn1, ccolumn2, ccolumn3]
cdiag1 = [1,5,9]
cdiag2 = [3,5,7]
calldiag = [cdiag1,cdiag2]


new_list = [1,2,3,4,5,6,7,8,9]  #this is the real tic tac toe board

def print_board():
    print(f'_{new_list[0]}_|_{new_list[1]}_|_{new_list[2]}_')
    print(f'_{new_list[3]}_|_{new_list[4]}_|_{new_list[5]}_')
    print(f'_{new_list[6]}_|_{new_list[7]}_|_{new_list[8]}_')
    print("")

def player():
    while True:  #puting the input in a loop and it will only break if you put in a number on the board and that number is not already made
        copy = 0
        move = input(("what move do you want to make? "))
        if move == "1" or move == "2" or move == "3" or move == "4" or move == "5" or move == "6" or move == "7" or move == "8" or move == "9":
            copy = copy + 1
            move = int(move)
            move = move-1
            if new_list[move]!="o" and new_list[move]!="x":
                copy = copy +1
            move = move +1
        if copy == 2:
            break
    player_moves.append(move)
    move = move-1
    new_list[move] = "o"
    for column in allcolumns:  #this goes through all the player columns/rows/diagonals and removes that move from all of them
        if (move+1) in column:
            column.remove(move+1)  #removes the last move from the columns
            print(column)
    for row in allrows:
        if (move+1) in row:
            row.remove(move+1)
            print(row)
    for diag in alldiag:
        if (move+1) in diag:
            diag.remove(move+1)
            #print("still player")
            print(diag)

def computer():
    move = 0
    while True:
        if new_list[4] != "o" and new_list[4]!="x":
            new_list[4] = "x"
            computer_moves.append(5)
            move=5
            for column in callcolumns: #find what row/column/diagonal the move is in and gets rid of it from there to keep track of what moves have been made
                if (move) in column:
                    column.remove(move)  #removes the last move from the columns
            for row in callrows:
                if (move) in row:
                    row.remove(move)
            for diag in calldiag:
                if (move) in diag:
                    diag.remove(move)
            #print("move 5")
            return
        else:
            #print("in else")
            for row in allrows:
                print(row)
                if len(row)==1:
                    if new_list[(row[0]-1)]!="o" and new_list[(row[0]-1)]!="x":
                        new_list[(row[0]-1)] = "x"
                        computer_moves.append(row[0])
                        move = row[0]
                        row.remove(row[0])
                        #print("work1")
                        return
            for column in allcolumns:
                print(column)
                if len(column) == 1:
                    if new_list[(column[0]-1)] != "o" and new_list[(column[0]-1)]!="x":
                        print(column[0])
                        new_list[(column[0]-1)] = "x"
                        computer_moves.append(column[0])
                        move = column[0]
                        column.remove(column[0])
                        #print("work2")
                        return
            for row in callrows:
                print(row)
                if len(row)==1:
                    if new_list[(row[0]-1)] !="x" and new_list[(row[0]-1)]!="o":
                        new_list[(row[0]-1)] = "x"
                        computer_moves.append(row[0])
                        move = row[0]
                        row.remove(row[0])
                        #print("work3")
                        return
            for column in callcolumns:
                print(column)
                if len(column) == 1:
                    if new_list[(column[0]-1)] != "x" and new_list[(column[0]-1)] != "o":
                        new_list[(column[0]-1)] = "x"
                        computer_moves.append(column[0])
                        move = column[0]
                        column.remove(column[0])
                        #print("work4")
                        return
            for diag in alldiag:
                print(diag)
                if len(diag) ==1:
                    if new_list[(diag[0]-1)] != "x" and new_list[(diag[0]-1)] != "o": #making sure that it is not effected because of how it will first take middle if player doesn't
                        new_list[(diag[0]-1)] = "x"
                        computer_moves.append(diag[0])
                        move = diag[0]
                        diag.remove(diag[0])
                        #print("new work 1")
                        return
            for diag in calldiag:
                print(diag)
                if len(diag) ==1:
                    if new_list[(diag[0]-1)] !="o" and new_list[(diag[0]-1)] != "x": 
                        new_list[(diag[0]-1)] = "x"
                        computer_moves.append(diag[0])
                        move = diag[0]
                        diag.remove(diag[0])
                        #print("new work 2")
                        return
            if move == 0:
                while True:
                    move = random.randint(0,8)
                    if new_list[move] != "o" and new_list[move] != "x":
                        new_list[move] = "x"
                        computer_moves.append(move+1)
                        for column in callcolumns:#find what row/column/diagonal the move is in and gets rid of it from there to keep track of what moves have been made
                            if (move+1) in column:
                                column.remove(move+1)  
                        for row in callrows:
                            if (move+1) in row:
                                row.remove(move+1)
                        for diag in calldiag:
                            if (move+1) in diag:
                                diag.remove(move+1)
                        #print("random")
                        return
        
def check_win():
    for eachlist in winning_moves: #check if the player_moves or computer_moves contain the winning moves if they do someone wins
        if set(eachlist).issubset(player_moves) == True:
            print("player wins")
            exit()
        if set(eachlist).issubset(computer_moves) == True:
            print("computer wins")
            exit()

def check_tie():
    totalmoves=0
    for i in new_list:
        if i=="x" or i=="o":
            totalmoves= totalmoves+1
    if totalmoves == 9:
        print("tie")
        exit()

def main():
    print_board()
    while True:
        player()
        print_board()
        check_win()
        check_tie()
        computer()
        print_board()
        check_win()
        check_tie()
main()