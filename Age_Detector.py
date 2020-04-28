
print("...WELCOME TO AGE CALCULATOR...")

def func(ageYear):                          # function definition
    '''...This function takes age and year of a user and tells the year when he/she will turn 100 year and 
    ask the user optionally to know thier age in a particular year....'''
    
    
    if len(ageYear)==4:
        currentYear = 2020
        if int(ageYear) > currentYear:
            print(f"Are you Ghost! You are not born yet!\n This is {currentYear}")
            quit()

        else:
            current_age=currentYear-int(ageYear)
            print(f"You are now {current_age} year old")
            n = 100 - current_age
            century = currentYear + n
            if century > 2020:
                print(f"You will turn 100 year in {century}")
            else:
                print(f"You turned 100 in {century}")

    elif int(ageYear) >= 0 or int(ageYear) <= 125:
        
        currentYear = 2020
        current_age = int(ageYear)
        if current_age > 100:
            print(f"You seems too old ...")
        print(f"You are now {current_age} year old ")
        n = 100 - current_age
        century = currentYear + n
        if century > 2020:
            print(f"You will turn 100 in {century}")
        else:
            print(f"You turned 100 in {century}")


    print(f"Do you want to know how many year old you are in a particular year?")
    inp = input("Press y for yes and n for no : ")
    if inp == 'n':
        quit()
    elif inp == 'y':
        currentYear = 2020
        if len(ageYear) == 4:
            year = int(input("Enter the year : "))
            y = year-int(ageYear)
            if year > currentYear:
                print(f"You will be {y} year in {year} ")
            else:
                print(f"You were {y} year in {year}")
        else:
            year = int(input("Enter the year : "))
            
            if year > currentYear:
                year_current = year-2020
                year_current += 100 
                print(f"You will be {year_current} year in {year} ")
            else:
                year_current = 2020-year
                year_current += 100 
                print(f"You were {year_current} year in {year}")

     
ageYear=input("Enter your age or year of birth ")   # taking input
print(func(ageYear))                                # calling function