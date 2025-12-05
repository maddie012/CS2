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

        def age_analysis():
            total = 0
            allage = 0
            maxage = 0
            minage = 0
            survived = 0
            died = 0
            agesurv = 0
            agedead=0

            for line in file:
                row = line.strip().split(',')
                total += 1
                if row[6] != "":
                    age = int(row[6])
                    allage += age
                    if age > maxage:
                        age = maxage
                    if age < minage:
                        age = minage
                    if row[1] == "1":
                        survived +=1
                        agesurv += int(row[6])
                    else:
                        died+=1
                        agedead += int(row[6])

            print(f'Average age: {allage/total}')
            print(f'The oldest passenger is {maxage}')
            print(f'The youngest passenger is: {minage}')



        
        def main():
            ten_rows()
            survival_rate()
            age_analysis()
        main()
        
except FileNotFoundError:
    print("Error: 'titanic.csv' file not found.")
    