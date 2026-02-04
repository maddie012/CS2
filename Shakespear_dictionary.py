
Hamlet_dict = {}
def shakespeare_Hamlet():
    with open('Hamlet.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word not in Hamlet_dict:
                    Hamlet_dict[word] = 1
                else:
                    Hamlet_dict[word] = Hamlet_dict[word] + 1
        for key in list(Hamlet_dict.keys()):
            if (Hamlet_dict[key]) < 10:
                del Hamlet_dict[key]
        for x, y in Hamlet_dict.items():
            print(x, y)
shakespeare_Hamlet()
