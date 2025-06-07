import time
def MainMenu():
    print("Sleep Tracking: (1)")
    print("Mood Tracking: (2)")
    print("Spending Tracking: (3)")
    print("Book Logs: (4)")
    print("Game Tracking: (5)")
    print("Study Tracking: (6)")
    print("Exit: (7)")

def Process():
    print("Append: (1)")
    print("Read: (2)")
    print("Remove log: (3)")
    print("rewrite: (4)")
    print("Search: (5)")
    print("summary: (6)")    

def SleepTracking(x):
    if x == 1:
        with open("SleepTracking.txt", "a") as st:
            SleepTime = int(input("How many hours did you sleep (round to nearest hour): "))
            st.write(f"{SleepTime} hours of sleep\n")
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 2:
        with open("SleepTracking.txt", "r") as st:
            for NewLine in st:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
    if x == 3:
        with open("SleepTracking.txt", "w") as st:
            pass
    if x == 4:
        with open("SleepTracking.txt", "4") as st:
            pass
    if x == 5:
        with open("SleepTracking.txt", "r") as st:
            pass
    if x == 6:
        with open("SleepTracking.txt", "r") as st:
            pass
def MoodTracking(x):
    pass

def SpendingTracking(x):
    pass

def BookLogs(x):
    pass

def GameTracking(x):
    pass

def StudyTracking(x):
    pass


while True: #mainloop
    MainMenu()
    while True:
        try:
            TrackerChoice = int(input("Enter Assigned Number of Tracker to acess: "))
            if TrackerChoice <= 7 and TrackerChoice >= 1:
                break
            else:
                print("Enter number between 1 and 7")
                continue
        except ValueError:
            print("Enter valid integer")
    if TrackerChoice == 7:
        while True:
            try:
                leaving = int(input("Do you want to exit?\n yes(1)/no(2): "))
                if leaving == 1 or leaving == 2:
                    break
                else:
                    print("Enter values 1(yes) or 2(no)")
                    continue
            except ValueError:
                print("enter valid integer")
        if leaving == 1:
            print("bye")
            break
        else:
            print("ok continuing...")
            time.sleep(2)
            continue
    Process()
    while True:
        try:
            ProcessChoice = int(input("Enter Assigned Number of process to run: "))
            if ProcessChoice >= 1 and ProcessChoice <= 6:
                break
            else:
                print("Enter valid number between 1 and 6")
        except ValueError:
            print("Enter an Integer")
    if TrackerChoice == 1:
        SleepTracking(ProcessChoice)
    if TrackerChoice == 2:
        MoodTracking(ProcessChoice)
    if TrackerChoice == 3:
        SpendingTracking(ProcessChoice)
    if TrackerChoice == 4:
        BookLogs(ProcessChoice)
    if TrackerChoice == 5:
        GameTracking(ProcessChoice)
    if TrackerChoice == 6:
        StudyTracking(ProcessChoice)
    
    
    
    


    

