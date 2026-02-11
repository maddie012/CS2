#Author: Madeleine Elias
#Date: 2/5/26
#Description: sees how many times each words are used in plays Hamlet and The Tempest
#Bugs:
#Challenges:
#Sources: W3schools, google
#Log: 1.1

import csv

boring_words= ["the", "of", "i", "a", "before", "at", "his", "to", "him", "me", "which", "did", "by", "more", "than", "mine", "own", "as", "such", "was", "and", "very", "he", "on", "you", "come", "an", "your", "some", "for", "does", "this", "can", "there", "goes", "am", "even", "have", "those", "had", "not", "been", "here", "of", "do", "these", "my", "almose", "them", "still", "is", "though", "our", "any", "us", "with", "that", "it", "are", "so", "or", "they", "about", "lets", "ever", "we", "yet", "thats", "out", "from", "things", "where", "whats", "myself", "cannot", "then", "seem", "in", "should", "like", "her", "would", "itself", "be", "into", "she", "were", "saw", "their", "each", "while", "else", "himself", "keep", "way","every","said" ,"many","makes","since" ,"after","another","could","theres","hes" ,"cause" ,"most" ,"upon" ,"now","much","if" ,"make" ,"give" ,"who","has","say","what","thing","again","but","once","last","when","Thou", "thy", "thee", "therefore", "tis", "ho", "o", "hath", "let", "may", "awhile", "made", "off", "comes", "art", "might", "thus", "doth", "whose", "why", "ist", "hast", "use", "shall", "ourselves", "twere", "further", "must", "thine", "ay", "indeed", "put", "mean", "alas", "aught", "ha", "dost", "thou", "heard","rather", "till", "within","both", "hither", "didst","shalt", "tell", "em","whom", "nor", "too", "aside", "how", "ill"]

def hamlet():
    hamlet_dict = {}
    with open('Hamlet.txt', 'r') as file:
        for line in file:
            words = line.split()
            
            for word in words:
                word = word.lower()
                
                if word not in hamlet_dict:
                    hamlet_dict[word] = 1
                else:
                    hamlet_dict[word] += 1
        for key in list(hamlet_dict.keys()):
            if (hamlet_dict[key]) < 10:
                del hamlet_dict[key]
            elif key in boring_words:
                del hamlet_dict[key]
        print("Most Common words in Hamlet")
        
        #for x, y in hamlet_dict.items():
            #print(x, y)
        asc = {k: v for k, v in sorted(hamlet_dict.items(), key=lambda item: item[1])}
        for x,y in asc.items():
            print(x,y)
        sorted_asc = dict(asc)
        hamlet_words = list(sorted_asc.keys())
        hamlet_values = list(sorted_asc.values())
        return hamlet_dict, hamlet_words, hamlet_values

def tempest():
    tempest_dict = {}
    with open('The Tempest.txt', 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                word = word.lower()

                if word not in tempest_dict:
                    tempest_dict[word] = 1
                else:
                    tempest_dict[word] += 1
        for key in list(tempest_dict.keys()):
            if (tempest_dict[key]) < 10:
                del tempest_dict[key]
            elif key in boring_words:
                del tempest_dict[key]
        print("Most common words in The Tempest")
        asc = {k: v for k, v in sorted(tempest_dict.items(), key=lambda item: item[1])}
        for x,y in asc.items():
            print(x,y)
        sorted_asc = dict(asc)
        tempest_words = list(sorted_asc.keys())
        tempest_values = list(sorted_asc.values())
        return tempest_dict, tempest_words, tempest_values
    
def make_file(hamlet_dict):
    fieldnames= ["words in hamlet", "hamlet_values", "words in tempest", "tempest_values"]
    filename= "shakespeare fequency.csv"
    with open(filename, mode = 'w', newline= '') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writeheader()
        for i in range(len(hamlet_dict["words in hamlet"])):
            if len(hamlet_dict["words in tempest"]) > i: 
                writer.writerow([hamlet_dict["words in hamlet"][i], hamlet_dict["hamlet_values"][i], hamlet_dict["words in tempest"][i], hamlet_dict["tempest_values"][i]])
            else:
                writer.writerow([hamlet_dict["words in hamlet"][i], hamlet_dict["hamlet_values"][i], None, None])
        '''for key, value in hamlet_dict.items():
            writer.writerow([key, value])'''

def other_dict(hamlet_words, hamlet_values, tempest_words, tempest_values):
    new_dict = {"words in hamlet": hamlet_words, "hamlet_values":hamlet_values, "words in tempest": tempest_words, "tempest_values":tempest_values}
    return new_dict


hamlet_dict, hamlet_words, hamlet_values = hamlet()
tempest_dict, tempest_words, tempest_values = tempest()
new_dict = other_dict(hamlet_words, hamlet_values, tempest_words, tempest_values)
make_file(new_dict)
