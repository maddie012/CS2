#tictactoe2
import random
#Computer is x
#player 2 is x
#player is o
winning_moves= [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

#columns = (1,2,3)
#rows = (1,2,3)
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
'''


def print_board():
    print(f"{row1[0] and column1[0]}|{row1[1] and column2[1]}|{row1[2] and column3[2]}")
    print(f"{row2[0] and column1[0]}|{row2[1] and column2[1]}|{row2[2] and column3[2]}")
    print(f"{row3[0] and column1[0]}|{row3[1] and column2[1]}|{row3[2] and column3[2]}")

def player():
    whichrow = input("what row is you move in? ")
    whichcolumn = int(input("what column is your move in? "))
    if whichrow == "1":
        thecolumn = row1.index(whichcolumn)'''

new_list = [1,2,3,4,5,6,7,8,9]

def print_board():
    print(f'_{new_list[0]}_|_{new_list[1]}_|_{new_list[2]}_')
    print(f'_{new_list[3]}_|_{new_list[4]}_|_{new_list[5]}_')
    print(f'_{new_list[6]}_|_{new_list[7]}_|_{new_list[8]}_')
    print("")

def player():
    '''whichrow = int(input("what row is you move in? "))
    whichcolumn = int(input("what column is your move in? "))'''
    move = input(("what move do you want to make? "))
    try: 
        move = int(move)
    except ValueError as verr:
        print("enter integer")
    player_moves.append(move)
    move = move-1
    new_list[move] = "o"
    for column in allcolumns:
        if (move+1) in column:
            column.remove(move+1)  #removes the last move from the columns
            print(column)
            this_column = column
    for row in allrows:
        if (move+1) in row:
            row.remove(move+1)
            #print("still player")
            print(row)
            this_row = row
    for diag in alldiag:
        if (move+1) in diag:
            diag.remove(move+1)
            print("still player")
            print(diag)
    '''if this_row == row1:
        rrow = 1
    elif this_row == row2:
        rrow = 2
    else:
        rrow = 3
    if this_column == column1:
        rcolumn = 1
    elif this_column == column2:
        rcolumn = 2
    else:
        rcolumn = 3
    common0 = set(this_column) & set(this_row)
    common0 = set(this_column).intersection(this_row)
    #common = int(common0)
    #common0 = common0-1
    return rrow, rcolumn'''


def computer():
    move = 0
    #allrows = [row1, row2, row3]
    #allcolumns = [column1, column2, column3]
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

            print("move 5")
            return
        else:
            print("in else")
            for row in allrows:
                print(row)
                if len(row)==1:
                    if new_list[(row[0]-1)]!="o" and new_list[(row[0]-1)]!="x":
                        new_list[(row[0]-1)] = "x"
                        computer_moves.append(row[0])
                        move = row[0]
                        row.remove(row[0])
                        ("work1")
                        return
            for column in allcolumns:
                print(column)
                if len(column) == 1:
                    if new_list[(column[0]-1)] != "o" and new_list[(column[0]-1)]!="x":
                        print(column[0])
                        #num = (column[0])
                        #idexednum = num-1
                        new_list[(column[0]-1)] = "x"
                        #new_list[idexednum] = "x"
                        computer_moves.append(column[0])
                        move = column[0]
                        column.remove(column[0])
                        print("work2")
                        return
            for row in callrows:
                print(row)
                if len(row)==1:
                    if new_list[(row[0]-1)] !="x" and new_list[(row[0]-1)]!="o":
                        new_list[(row[0]-1)] = "x"
                        computer_moves.append(row[0])
                        move = row[0]
                        row.remove(row[0])
                        print("work3")
                        return
            for column in callcolumns:
                print(column)
                if len(column) == 1:
                    if new_list[(column[0]-1)] != "x" and new_list[(column[0]-1)] != "o":
                        new_list[(column[0]-1)] = "x"
                        computer_moves.append(column[0])
                        move = column[0]
                        column.remove(column[0])
                        print("work4")
                        return
            for diag in alldiag:
                print(diag)
                if len(diag) ==1:
                    if new_list[(diag[0]-1)] != "x" and new_list[(diag[0]-1)] != "o": #making sure that it is not effected because of how it will first take middle if player doesn't
                        new_list[(diag[0]-1)] = "x"
                        computer_moves.append(diag[0])
                        move = diag[0]
                        diag.remove(diag[0])
                        print("new work 1")
                        return
            for diag in calldiag:
                print(diag)
                if len(diag) ==1:
                    if new_list[(diag[0]-1)] !="o" and new_list[(diag[0]-1)] != "x": 
                        new_list[(diag[0]-1)] = "x"
                        computer_moves.append(diag[0])
                        move = diag[0]
                        diag.remove(diag[0])
                        print("new work 2")
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
                        print("random")
                        return
                        #break
                    
            #if move != 0:
                #new_list[{move-1}] = "x"
                #computer_moves.append(move)
                #break
            #else:
        

def check_win():
    for eachlist in winning_moves:
        if set(eachlist).issubset(player_moves) == True:
            print("win")
            exit()
        if set(eachlist).issubset(computer_moves) == True:
            print("win")
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