#Author: Madeleine Elias
#Date: 2/5/26
#Description: sees how many times each words are used in plays Hamlet and The Tempest
#Bugs:
#Challenges:
#Sources: W3schools, google, teachers
#Log: 1.3

import csv

boring_words= ["the", "of", "i", "a", "before", "at", "his", "to", "him", "me", "which", "did", "by", "more", "than", "mine", "own", "as", "such", "was", "and", "very", "he", "on", "you", "come", "an", "your", "some", "for", "does", "this", "can", "there", "goes", "am", "even", "have", "those", "had", "not", "been", "here", "of", "do", "these", "my", "almose", "them", "still", "is", "though", "our", "any", "us", "with", "that", "it", "are", "so", "or", "they", "about", "lets", "ever", "we", "yet", "thats", "out", "from", "things", "where", "whats", "myself", "cannot", "then", "seem", "in", "should", "like", "her", "would", "itself", "be", "into", "she", "were", "saw", "their", "each", "while", "else", "himself", "keep", "way","every","said" ,"many","makes","since" ,"after","another","could","theres","hes" ,"cause" ,"most" ,"upon" ,"now","much","if" ,"make" ,"give" ,"who","has","say","what","thing","again","but","once","last","when","Thou", "thy", "thee", "therefore", "tis", "ho", "o", "hath", "let", "may", "awhile", "made", "off", "comes", "art", "might", "thus", "doth", "whose", "why", "ist", "hast", "use", "shall", "ourselves", "twere", "further", "must", "thine", "ay", "indeed", "put", "mean", "alas", "aught", "ha", "dost", "thou", "heard","rather", "till", "within","both", "hither", "didst","shalt", "tell", "em","whom", "nor", "too", "aside", "how", "ill"]
#boring_words is the list of words i don't want to be in the output of the code

def hamlet():
    '''Description: it finds out how many times each word is used in the play and removes the ones that were used less than 10 times and the ones that were in boring words
    Args: none
    Returns: 
        hamlet_dict: the dictionary of the word that is used and the number of times they are used
        hamlet_words: a list of just the words that are used
        hamlet_values: a list of the number of times they are used'''
    hamlet_dict = {}
    with open('Hamlet.txt', 'r') as file:
        for line in file:
            words = line.split()
            
            for word in words:
                word = word.lower() #make every word lowercase so it doesn't count the same word multiple times
                
                if word not in hamlet_dict:  #if the word is not already there it makes it one
                    hamlet_dict[word] = 1
                else:
                    hamlet_dict[word] += 1
        for key in list(hamlet_dict.keys()):  #if the value is less then 10 it wont return them and delete from dict
            if (hamlet_dict[key]) < 10:
                del hamlet_dict[key]
            elif key in boring_words:
                del hamlet_dict[key]
        print("Most Common words in Hamlet")
        asc = {k: v for k, v in sorted(hamlet_dict.items(), key=lambda item: item[1])}  #sorts the dict by the value in increasing order as tuple
        for x,y in asc.items():
            print(x,y)
        sorted_asc = dict(asc)  #turns it back into list
        hamlet_words = list(sorted_asc.keys())
        hamlet_values = list(sorted_asc.values())
        return hamlet_dict, hamlet_words, hamlet_values

def tempest():
    '''Description: it finds out how many times each word is used in the play and removes the ones that were used less than 10 times and the ones that were in boring words
    Args: none
    Returns: 
        tempest_dict: the dictionary of the word that is used and the number of times they are used
        tempest_words: a list of just the words that are used
        tempest_values: a list of the number of times they are used'''
    tempest_dict = {}
    with open('The Tempest.txt', 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                word = word.lower()#make every word lowercase so it doesn't count the same word multiple times

                if word not in tempest_dict:  #if the word is not already there it makes it one
                    tempest_dict[word] = 1
                else:
                    tempest_dict[word] += 1
        for key in list(tempest_dict.keys()):#if the value is less then 10 it wont return them and delete from dict
            if (tempest_dict[key]) < 10:
                del tempest_dict[key]
            elif key in boring_words:
                del tempest_dict[key]
        print("Most common words in The Tempest")
        asc = {k: v for k, v in sorted(tempest_dict.items(), key=lambda item: item[1])}  #sorts the dict by the value in increasing order as tuple
        for x,y in asc.items():
            print(x,y)
        sorted_asc = dict(asc) #turns it back into list
        tempest_words = list(sorted_asc.keys())
        tempest_values = list(sorted_asc.values())
        return tempest_dict, tempest_words, tempest_values
    
def make_file(new_dict):
    '''Description: takes a dictionary consisting of what other functions have gotton from Hamlet and the Tempest and puts them into a file 
    Args:
        new_dict: a dictionary that has lists inside of it from the words in hamlet and values and words in tempest and values
    Returns:
        new file with information'''
    filename= "shakespeare fequency.csv"
    with open(filename, mode = 'w', newline= '') as csvfile:  #makes new csv file 
        writer = csv.writer(csvfile)
        for i in range(len(new_dict["words in hamlet"])): #since hamlet has more it uses the length of it
            if len(new_dict["words in tempest"]) > i:  #if there is enough words in tempest for that one
                writer.writerow([new_dict["words in hamlet"][i], new_dict["hamlet_values"][i], new_dict["words in tempest"][i], new_dict["tempest_values"][i]]) #adds another row that has all of them
            else:  #else there isn't enough words in tempest
                writer.writerow([new_dict["words in hamlet"][i], new_dict["hamlet_values"][i], None, None]) #adds row with the hamlet data but not tempest b/c there isn't enough
    

def other_dict(hamlet_words, hamlet_values, tempest_words, tempest_values):
    '''Description: it takes what was taken from other functions and puts them all in one new dictionary
    Args:
        hamlet_words: a list of just the words that are used
        hamlet_values: a list of the number of times they are used
        tempest_words: a list of just the words that are used
        tempest_values: a list of the number of times they are used
    Returns:
        new_dict: a dictionary that has lists inside of it from the words in hamlet and values and words in tempest and values'''
    new_dict = {"words in hamlet": hamlet_words, "hamlet_values":hamlet_values, "words in tempest": tempest_words, "tempest_values":tempest_values} #makes a new dict which the values are the lists of the information about the words and values of the plays
    return new_dict


hamlet_dict, hamlet_words, hamlet_values = hamlet()
tempest_dict, tempest_words, tempest_values = tempest()
new_dict = other_dict(hamlet_words, hamlet_values, tempest_words, tempest_values)
make_file(new_dict)
