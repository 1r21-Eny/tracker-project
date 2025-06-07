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
#Sleep tracking
#Mood tracking
#Spending tracker
#Book logs
#game tracker
#study tracking
#main loop

while True:
    MainMenu()
    while True:
        try:
            TrackerChoice = int(input("Enter Assigned Number of Tracker to acess: "))
            break
        except ValueError:
            print("Enter valid integer")
    Process()
    while True:
        try:
            ProcessChoice = int(input("Enter Assigned Number of process to run: "))
            break
        except ValueError:
            print("Enter an Integer")
    
    
    

