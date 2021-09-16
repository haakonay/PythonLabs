#!/usr/bin/python


days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
dayDict = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat', 7: 'Sun'}

# Initializing empty lists
monSchedule, tueSchedule, wedSchedule, thuSchedule, friSchedule, satSchedule, sunSchedule = ([] for i in range(7))

# Appending lists with formatted time
for i in range(0, 22):
    monSchedule.append(f"{i}:00")
    tueSchedule.append(f"{i}:00")
    wedSchedule.append(f"{i}:00")
    thuSchedule.append(f"{i}:00")
    friSchedule.append(f"{i}:00")
    satSchedule.append(f"{i}:00")
    sunSchedule.append(f"{i}:00")

# Dictionary for use when grabbing lists based on user input (the key)
testDict = {"mon": monSchedule, "tue": tueSchedule, "wed": wedSchedule, "thu": thuSchedule, "fri": friSchedule, "sat": satSchedule, "sun": sunSchedule}

choice = 0

while choice != "x":

    print("s - store program\n")
    print("l - list daily program\n")
    print("x - exit\n")
    choice = input(" Choose from list:  ")
    if choice == "x":   # Breaks if user wants to e(x)it
        break
    elif choice == 'l':
        usrDay = input("what day?")
        print(*testDict[usrDay], sep="\n")  # '*' separates '[]', only listing the values.
                                            # 'Sep' separates each value with a new line.
    elif choice == 's':
        usrDay = input("\nWhich day?\n ")
        usrTime = int(input("What time?\n"))
        usrProg = input("What program?\n")
        #  Replacing a specific day with users day and program
        #  Each schedule from the dictionary is filled with times in a format
        (testDict[usrDay])[usrTime] = f"{usrTime}:00 {usrProg}"


