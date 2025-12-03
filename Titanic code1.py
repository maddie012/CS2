try:
    with open('titanic.csv', 'r') as file:
        #header = file.readline().strip().split(',')  # Read the header row
        #name_index = header.index('Name')  # Find the index of 'Name' column
        def ten_rows():
            rownum=0
            for line in file:
                row = line.strip().split(',')
                print(row)
                rownum +=1
                if rownum == 11:
                    break
                else:
                    rownum +=0
            #print(row[name_index])

        def survival_rate():
            total = 0
            survived = 0
            totalgrl = 0
            totalbys = 0
            survgrl = 0
            survbys = 0


            for line in file:
                row = line.strip().split(',')
                total += 1

                if row[5] == "female":
                    totalgrl += 1

                    if row[1] == "1":
                        survgrl += 1
                        survived +=1
                else:
                    totalbys +=1

                    if row[1] == "1":
                        survbys +=1
                        survived +=1
            print(f'Total Survival Rate: {survived/total*100}%')
            print(f'Female Survival Rate: {survgrl/totalgrl*100}%')
            print(f'Male Survival Rate: {survbys/totalbys*100}%')

        def check():
            check = "working"
            print(check)
        
        def main():
            ten_rows()
            survival_rate()
            check()
        main()
        
except FileNotFoundError:
    print("Error: 'titanic.csv' file not found.")
    