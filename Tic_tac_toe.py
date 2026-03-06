#tic tac toe
import random
new_list = ['1','2','3','4','5','6','7','8','9']
#Computer is x
#player is o
#winning moves: [1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]
win1 = [1,2,3]
win2 = [4,5,6]
win3 = [7,8,9]
win4 = [1,4,7]
win5 = [2,5,8]
win6 = [3,6,9]
win7 = [1,5,9]
win8 = [3,5,7]
player_moves = []
computer_moves = []  
player2_moves = []

def print_board():
    print(f'_{new_list[0]}_|_{new_list[1]}_|_{new_list[2]}_')
    print(f'_{new_list[3]}_|_{new_list[4]}_|_{new_list[5]}_')
    print(f'_{new_list[6]}_|_{new_list[7]}_|_{new_list[8]}_')
    print("")

def player():
    move = input("what move do you want to make ")
    if move == "1" and new_list[0]!= "x" and new_list[0]!="o":
        new_list[0] = "o"
        player_moves.append(1)
    elif move == "2" and new_list[1]!= "x" and new_list[1]!="o":
        new_list[1] = "o"
        player_moves.append(2)
    elif move == "3" and new_list[2]!= "x" and new_list[2]!="o":
        new_list[2] = "o"
        player_moves.append(3)
    elif move == "4" and new_list[3]!= "x" and new_list[3]!="o":
        new_list[3] = "o"
        player_moves.append(4)
    elif move == "5" and new_list[4]!= "x" and new_list[4]!="o":
        new_list[4] = "o"
        player_moves.append(5)
    elif move == "6" and new_list[5]!= "x" and new_list[5]!="o":
        new_list[5] = "o"
        player_moves.append(6)
    elif move == "7"and new_list[6]!= "x" and new_list[6]!="o":
        new_list[6] = "o"
        player_moves.append(7)
    elif move == "8" and new_list[7]!= "x" and new_list[7]!="o":
        new_list[7] = "o"
        player_moves.append(8)
    elif move == "9" and new_list[8]!= "x" and new_list[8]!="o":
        new_list[8] = "o"
        player_moves.append(9)
    else:
        print("Write your move ")
        player()

def player2():
    move = input("what move do you want to make ")
    if move == "1" and new_list[0]!= "x" and new_list[0]!="o":
        new_list[0] = "x"
        player2_moves.append(1)
    elif move =="2" and new_list[1] != "x" and new_list[1]!="o":
        new_list[1] = "x"
        player2_moves.append(2)
    elif move =="3" and new_list[2] != "x" and new_list[2]!="o":
        new_list[2] = "x"
        player2_moves.append(3)
    elif move =="4" and new_list[3] != "x" and new_list[3]!="o":
        new_list[3] = "x"
        player2_moves.append(4)
    elif move =="5" and new_list[4] != "x" and new_list[4]!="o":
        new_list[4] = "x"
        player2_moves.append(5)
    elif move =="6" and new_list[5] != "x" and new_list[5]!="o":
        new_list[5] = "x"
        player2_moves.append(6)
    elif move =="7" and new_list[6] != "x" and new_list[6]!="o":
        new_list[6] = "x"
        player2_moves.append(7)
    elif move =="8" and new_list[7] != "x" and new_list[7]!="o":
        new_list[7] = "x"
        player2_moves.append(8)
    elif move =="9" and new_list[8] != "x" and new_list[8]!="o":
        new_list[8] = "x"
        player2_moves.append(9)
    else:
        print("write your moves")
        player2()

    

def computer():
    if new_list[4] != "o" and new_list[4] != "x":
        new_list[4] = "x"
        computer_moves.append(5)
    elif new_list[0] != "o" and new_list[0] !="x" and ((new_list[1] == "o" and new_list[2] =="o")or (new_list[3] =="o" and new_list[6] =="o")or (new_list[4]=="o" and new_list[8]=="o")):
        new_list[0] = "x"
        computer_moves.append(1)
    elif new_list[1] != "o" and new_list[1] != "x" and ((new_list[0]=="o" and new_list[2]=="o") or (new_list[4]=="o" and new_list[7]=="o")):
        new_list[1] = "x"
        computer_moves.append(2)
    elif new_list[3] != "o" and new_list[3] !="x" and ((new_list[4] == "o" and new_list[5]=="o") or (new_list[0]=="o" and new_list[6]=="o")):
        new_list[3] = "x"
        computer_moves.append(4)
    else:
        move = random.randint(0,8)
        if new_list[move] != "o" and new_list[move] != "x":
            new_list[move] = "x"
            computer_moves.append(move+1)
        else:
            computer()

def check_win(player_moves, computer_moves):
    if (1 in player_moves and 2 in player_moves and 3 in player_moves):
        print("player1 wins")
        return "win"
    elif (4 in player_moves and 5 in player_moves and 6 in player_moves):
        print("player1 wins")
        return "win"
    elif (7 in player_moves and 8 in player_moves and 9 in player_moves):
        print("player1 wins")
        return "win"
    elif (1 in player_moves and 4 in player_moves and 7 in player_moves):
        print("player1 wins")
        return "win"
    elif (2 in player_moves and 5 in player_moves and 8 in player_moves):
        print("player1 wins")
        return "win"
    elif (3 in player_moves and 6 in player_moves and 9 in player_moves):
        print("player1 wins")
        return "win"
    elif (1 in player_moves and 5 in player_moves and 9 in player_moves):
        print("player1 wins")
        return "win"
    elif (3 in player_moves and 5 in player_moves and 7 in player_moves):
        print("player1 wins")
        return "win"
    elif (1 in computer_moves and 2 in computer_moves and 3 in computer_moves):
        print("player2 wins")
        return "win"
    elif (4 in computer_moves and 5 in computer_moves and 6 in computer_moves):
        print("player2 wins")
        return "win"
    elif (7 in computer_moves and 8 in computer_moves and 9 in computer_moves):
        print("player2 wins")
        return "win"
    elif (1 in computer_moves and 4 in computer_moves and 7 in computer_moves):
        print("player2 wins")
        return "win"
    elif (2 in computer_moves and 5 in computer_moves and 8 in computer_moves):
        print("player2 wins")
        return "win"
    elif (3 in computer_moves and 6 in computer_moves and 9 in computer_moves):
        print("player2 wins")
        return "win"
    elif (1 in computer_moves and 5 in computer_moves and 9 in computer_moves):
        print("player2 wins")
        return "win"
    elif (3 in computer_moves and 5 in computer_moves and 7 in computer_moves):
        print("player2 wins")
        return "win"
    else:
        return "no winner"
    
       

def check_tie():
    count2 = 0
    for number in range(9):
        if new_list[number-1] != "o" and new_list[number-1] != "x":
            count2 = count2 +1
    if count2 == 0:
        print("tie")
        return "tie"


#player()
#print_board()
#computer()
#print_board()

def main():
    question = input("play other person or computer p/c ")
    if question == "p":
        print("player1 is o and player2 is x")
        print_board()
        while True:
            player()
            persongame = check_win(player_moves, player2_moves)
            if persongame == "win":
                print_board()
                break
            end = check_tie()
            if end == "tie":
                print_board()
                break
            print_board()
            player2()
            print_board()
            persongame = check_win(player_moves, player2_moves)
            if persongame == "win":
                print_board()
                break
            end = check_tie()
            if end == "tie":
                print_board()
                break
    elif question == "c":
        print("player is o and computer is x")
        print_board()
        while True:
            player()
            game = check_win(player_moves, computer_moves)
            if game == "win":
                print_board()
                break
            end = check_tie()
            if end == "tie":
                print_board()
                break
            computer()
            print_board()
            game = check_win(player_moves, computer_moves)
            if game == "win":
                break
            end = check_tie()
            if end == "tie":
                break
    else:
        print("did not input correctly")
            
main()