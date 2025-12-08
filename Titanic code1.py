try:
    with open('titanic.csv', 'r') as file:
        #header = file.readline().strip().split(',')  # Read the header row
        #name_index = header.index('Name')  # Find the index of 'Name' column
        def ten_rows():
            file.seek(0)
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
            file.seek(0)
            total = 0
            survived = 0
            totalgrl = 0
            totalbys = 0
            survgrl = 0
            survbys = 0

            next(file)

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
            print(f'Total Survival Rate: {"{:.2f}".format(survived/total*100)}%')
            print(f'Female Survival Rate: {"{:.2f}".format(survgrl/totalgrl*100)}%')
            print(f'Male Survival Rate: {"{:.2f}".format(survbys/totalbys*100)}%')
            if(survgrl/totalgrl*100) > (survbys/totalbys*100):
                print("The women had a higher survival rate than the men")
            else:
                print("The men had a higher survival rate than women")

        def age_analysis():
            file.seek(0)
            total = 0
            allage = 0
            maxage = -1
            minage = 200
            survived = 0
            died = 0
            agesurv = 0
            agedead=0

            next(file)

            for line in file:
                row = line.strip().split(',')
                total += 1

                if row[6] != "":
                    age = float(row[6])
                    allage += age

                    if age > maxage:
                        usemth1 = age-maxage              #I have to use usemth1 and 2 because it was not working if I said  maxage = age or minage = age it was not changing maxage or minage
                        maxage += usemth1
                    if age < minage:
                        usemth2 = minage - age
                        minage -= usemth2

                    if row[1] == "1":
                        survived +=1
                        agesurv += float(row[6])
                    else:
                        died+=1
                        agedead += float(row[6])

            print(f'Average age: {"{:.2f}".format(allage/total)}')
            print(f'The oldest passenger is {maxage} years old')
            print(f'The youngest passenger is {minage} years old')

        def analysis_class():
            file.seek(0)
            total = 0
            all1 = 0
            surv1 = 0
            pay1 = 0 
            all2 = 0
            surv2 = 0
            pay2 = 0
            all3 = 0
            surv3 = 0
            pay3 = 0
            allpay = 0

            next(file)

            for line in file:
                row = line.strip().split(',')
                total += 1
                allpay += float(row[10])
                if row[2] == "1":
                    all1+=1
                    pay1+= float(row[10])
                    if row[1] == "1":
                        surv1 += 1
                elif row[2] == "2":
                    all2 += 1
                    pay2 += float(row[10])
                    if row[1] == "1":
                        surv2 += 1
                else:
                    all3 += 1
                    pay3 += float(row[10])
                    if row[1] == "1":
                        surv3+=1

            survrate1 = (surv1/all1)*100
            survrate2 = (surv2/all2)*100
            survrate3 = (surv3/all3)*100
            print(f'Survival rate of first class: {"{:.2f}".format(survrate1)}%')
            print(f'survival rate of second class: {"{:.2f}".format(survrate2)}%')
            print(f'survival rate of third class: {"{:.2f}".format(survrate3)}%')

            if survrate1>survrate2 and survrate1>survrate3:
                print("The first class passengers had a higher survival rate than both the other classes")
            if survrate2>survrate1 and survrate2>survrate3:
                print("the second class had the highest survival rate than both the other classes")
            if survrate3>survrate1 and survrate3>survrate2:
                print("the third class had the highest survival rate than both the other classes")

            print(f'Average fare: {"{:.2f}".format(allpay/total)}$')
            print(f'Average fare of 1st class: {"{:.2f}".format(pay1/all1)}$')
            print(f'Average fare of 2nd class: {"{:.2f}".format(pay2/all2)}$')
            print(f'Average fare of 3rd class: {"{:.2f}".format(pay3/all3)}$')

        '''def family_survival():
            with open('titanic.csv', 'w') as file:'''
            



        
        def main():
            ten_rows()
            survival_rate()
            age_analysis()
            analysis_class()
        main()
        
except FileNotFoundError:
    print("Error: 'titanic.csv' file not found.")
    