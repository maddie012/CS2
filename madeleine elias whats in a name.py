#author: Madeleine Elias
#date: 9/3/25
#description: asks for name or word and tests it with functions
#breaks: if they are any numbers or special characters, if they are less than three words or spaces,the frequency is off if there isn't three names, initials won't work if no middle name,
#challenges: makes random name from random letters, scrambles both first and full name
#sources: old codes, w3school


import random
def count_vowels(name):
    '''
    counts the vowels in the name and knows the totals of each vowel
    Args:
        name: the name that the user inputed 
    returns:
        the number of vowels in the name and the number of each vowel in the name'''
    a = 0
    e = 0
    ilet = 0
    o = 0
    u = 0
    y = 0
    count = 0
    for i in name:
        if i == "a" or i =="A":
            a = a + 1
            count = count +1
        elif i == "e" or i=="E":
            e = e +1
            count = count +1
        elif i == "i" or i=="I":
            ilet = ilet+1
            count = count+1
        elif i=="o" or i=="O":
            o=o+1
            count = count +1
        elif i=="u" or i=="U":
            u=u+1
            count + count +1
        elif i=="y" or i=="Y":
            y=y+1
            count = count +1
        else:
            count = count + 0
    message = f"A:{a} E:{e} I:{ilet} O:{o} U:{u} Y:{y} total:{count}"
    return message

def reverse_display(name):
    '''
    reverses the name and prints it
    Args:
        name: the name the user inputed
    returns:
        the name backwards'''
    return name[::-1]

def palindrome(name1):
    '''
    check if the name is a palindrome and prints true or false depending on if it is uses function lower to turn the first name to lowercase
    Args:
        name1: the first name of the user after the  full name got put into the function first_name()
    returns:
        true or false depending on the answer'''
    name2 = lower(name1)
    revname = name2[::-1]
    print(name2 == revname)

def count_consonant(name):
    '''counts the number of consonants by using for loops subtracts every time there is a space because it should not count for total letters
    Args:
        name: the name the user inputed
    returns:
        the number of consonants divided by the number of total charicters in the word'''
    total = 0
    for i in name:
        total = total + 1
    count = 0
    for i in name:
        if i == "q" or i =="w" or i =="r" or i=="t" or i=="p"or i=="s"or i=="d"or i=="f"or i=="g"or i=="h"or i=="j"or i=="k"or i=="l"or i=="z" or i=="x" or i=="c" or i=="v" or i=="b" or i=="n" or i=="m" or i=="Q" or i=="W" or i=="R" or i=="T" or i=="P" or i=="S" or i=="D" or i=="F" or i=="G" or i=="H" or i=="J" or i=="K" or i=="L" or i=="Z" or i=="X" or i=="C" or i=="V" or i=="B" or i=="N" or i=="M":
            count = count +1
        if i ==" ":
            total = total -1
        else:
            count = count + 0
    frequency = count/total
    return frequency

def first_name(name):
    '''
    finds the first name/word in what user inputed by stoping where the space is
    Args:
        name: the name the user inputed
    returns:
        the first name'''
    firname = ""
    for i in name:
        if i == " ":
            break
        else:
            firname += i
    return firname

def last_name(name):
    '''
    finds the last name by going backwards to find where the space is a turning it the right way again
    Args:
        name: the name the user inputed
    returns:
        The last name'''
    last = name[::-1]
    lstnm = ""
    for i in last:
        if i == " ":
            break
        else:
            lstnm += i
    rightnm = lstnm[::-1]
    return rightnm

def middle_name(name):
    '''
    finds the middle names by counting the idex until getting to the first space and then counts backwards until getting to the last space to get the index and then the middle name is what is between them. numfor is the count going forward and numback is the count going back
    Args:
        name: the name the user inputed
    returns:
        the middle names'''
    numfor = 0
    numback = len(name)
    for i in name:
        if i == " ":
            break
        else:
            numfor = numfor + 1
    numfor = numfor + 1
    for i in name[::-1]:
        if i == " ":
            break
        else:
            numback = numback - 1
    nim = (name[numfor:numback])
    return nim
    
def hyphen(name3):
    '''
    finds out if there is a hyphen in the last name using the function last_name
    Args:
        name3: last name of the user fron function last_name()
    returns:
        true or false depending if there is a hyphen in the last name'''
    random = 0
    for i in name3:
        if i == "-":
            return True
        else:
            random = random +0
    return False
            
def random_name():
    '''
    function chooses a random length between 5-15 for the length of the name. then it joins random letters for that length to get a random name
    Args:
        name: the name the user inputed
     returns:
        a random string of letters for the random name '''
    length = random.randint(5,15)
    return''.join(random.sample(list('qwertyuiopasdfghjklzxcvbnm'),length))

def initials(name1,name2,name3):
    '''
    function finds initials by first using the outputs of functions first_name, middle_name, last_name then converting them to list and printing the first letter of each using index
    Args:
        name1: the first name of the user after it got put into the function first_name()
        name2: the middle name of the user after it got put into the function middle_name()
        name3: the last name of the user after it got put into the function last_name()
    returns:
        initials of user input'''
    first = list(name1)
    middle = list(name2)
    last = list(name3)
    all = (first[0],middle[0],last[0])
    sep = ","
    initials = sep.join(all)
    return initials

def lower(name):
    '''
    function converts the letters to the octal value which is a letter to see if it is uppercase. If it is it adds 32 to convert it to its lowercase counterpart.
    Args:
        name: the name the user inputed
    returns:
        the name but will all characters as lowercase'''
    namout = ""
    for letter in name:
        if ord(letter)>64 and ord(letter)<91:
            num = ord(letter)
            num = num+32
            letter = chr(num)
            namout = namout+letter
        else:
            namout = namout+letter
    return namout

def upper(name):
    '''
    function converts letters to octel value and tests if they are lowercase. if they are it subtracts 32 to convert it to uppercase equivelant.
    Args:
        name: the name the user inputed
    returns:
        the name but with all characters as uppercase'''
    namout = ""
    for letter in name:
        if ord(letter)>96 and ord(letter)<123:
            num = ord(letter)
            num = num-32
            letter = chr(num)
            namout = namout+letter
        else:
            namout = namout+letter
    return namout

def title(name1):
    '''
    function finds out if the first name is a title and returns a boolean if it is true or false
    Args:
        name1: the full name of the user after it goes through the function first_name
    returns:
        true or false depending on if there is a title'''
    if name1 == "Dr." or name1=="Sir" or name1=="Esq" or name1=="Ph.d" or name1=="Professor" or name1=="Captain" or name1=="Ms" or name1=="Mrs" or name1=="Mr":
        return True
    else:
        return False

def mix_name(namef):
    '''
    function gets the first name from the function and scrambles it by making it into a list and picking random indexs to put into empty string
    Args:
        namef: the first name of the user after it goes through the function first name
    returns:
        a mix of the first name of the user'''
    mix = ""
    name1 = list(namef)
    while len(name1) > 0:
        namnum = len(name1) - 1
        number = random.randint(0,namnum)
        find = name1[number]
        mix += find
        name1.remove(find)
    return mix

def full_scramble(name):
    '''
    function uses the full name and scrambles it by turning it into a list and picking random indexs then deleting them to make original name smaller
    Args:
        name: the full name the user imported
    returns:
        a scramble of the users full name'''
    scramble = ""
    namel = list(name)
    while len(namel) > 0:
        namnum = len(namel) -1
        number = random.randint(0,namnum)
        find = namel[number]
        scramble += find
        namel.remove(find)
    return scramble



def main():
    name = input("enter your fullname (you need a middle name for all functions) ")
    print("what do you want to do?")
    name1 = first_name(name)
    name2 = middle_name(name)
    name3 = last_name(name)
    while True:
        question = input("vowels/reverse/consonants/random/first name/middle name/last name/uppercase/lowercase/initials/palindrome/hyphen/title/mix/scramble/exit ")

        if question =="vowels":
            print("number of vowels:")
            print(count_vowels(name))
        elif question =="reverse":
            print("reverse:")
            print(reverse_display(name))
        elif question == "consonants":
            print("frequency of consonants:")
            print(count_consonant(name))
        elif question == "random":
            print("random name:")
            print(random_name())
        elif question == "first name":
            print("first name:")
            print(first_name(name))
        elif question == "middle name":
            print("middle name:")
            print(middle_name(name))
        elif question == "last name":
            print("last name:")
            print(last_name(name))
        elif question == "uppercase":
            print("uppercase:")
            print(upper(name))
        elif question == "lowercase":
            print("lowercase:")
            print(lower(name))
        elif question == "initials":
            print("initials:")
            print(initials(name1,name2,name3))
        elif question == "palindrome":
            print("is it a palindrome")
            palindrome(name1)
        elif question == "hyphen":
            print("does it contain hyphen")
            print(hyphen(name3))
        elif question == "title":
            print("does it contain a title")
            print(title(name1))
        elif question == "mix":
            print("mix of first name")
            print(mix_name(name1))
        elif question == "scramble":
            print("scramble of full name")
            print(full_scramble(name))
        elif question == "exit":
            exit()
        else:
            print("choose an option ")
    
main()
     