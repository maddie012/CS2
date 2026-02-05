
hamlet_dict = {}
boring_words= ["the", "of", "i", "a", "before", "at", "his", "to", "him", "me", "which", "did", "by", "more", "than", "mine", "own", "as", "such", "was", "and", "very", "he", "on", "you", "come", "an", "your", "some", "for", "does", "this", "can", "there", "goes", "am", "even", "have", "those", "had", "not", "been", "here", "of", "do", "these", "my", "almose", "them", "still", "is", "though", "our", "any", "us", "with", "that", "it", "are", "so", "or", "they", "about", "lets", "ever", "we", "yet", "thats", "out", "from", "things", "where", "whats", "myself", "cannot", "then", "seem", "in", "should", "like", "her", "would", "itself", "be", "into", "she", "were", "saw", "their", "each", "while", "else", "himself", "keep", "way","every","said" ,"many","makes","since" ,"after","another","could","theres","hes" ,"cause" ,"most" ,"upon" ,"now","much","if" ,"make" ,"give" ,"who","has","say","what","thing","again","but","once","last","when","Thou", "thy", "thee", "therefore", "tis", "ho", "o", "hath", "let", "may", "awhile", "made", "off", "comes", "art", "might", "thus", "doth", "whose", "why", "ist", "hast", "use", "shall", "ourselves", "twere", "further", "must", "thine", "ay", "indeed", "put", "mean", "alas", "aught", "ha", "dost"]

def hamlet():
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
hamlet()

