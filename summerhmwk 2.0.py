import time
import datetime
def MainMenu():
    print("\nSleep Tracking: (1)")
    print("Socialising Tracking: (2)")
    print("Fitness Tracking: (3)")
    print("Book Tracking: (4)")
    print("Game Tracking: (5)")
    print("Revision Tracking: (6)")
    print("Exit: (7)")

def Process():
    print("\nAppend: (1)")
    print("Read: (2)")
    print("Remove log: (3)")
    print("rewrite: (4)")
    print("Search: (5)")
    print("summary: (6)")

def FileManagement(Tracker,Process):
    if Tracker == 1:
        File = "SleepTracking.txt"
        
    elif Tracker == 2:
        File = "SocialisationTracking.txt"
        
    elif Tracker == 3:
        File = "FitnessTracking.txt"
        
    elif Tracker == 4:
        File = "BookTracking.txt"
        
    elif Tracker == 5:
        File = "GameTracking.txt"
        
    elif Tracker == 6:
        File = "RevisionTracking.txt"
        
    elif Tracker == 7:
        pass
    
    if Process == 1:
        with open(File, "a") as f:
            Entry = int(input("How much have you spent doing your activity (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            LineToWrite = f"{date_str} - {Entry} hours Doing Activity\n"
            f.write(LineToWrite)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
            
    if Process == 2:
        with open(File, "r") as f:
            for NewLine in f:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
            
    if Process == 3:
        with open(File, "r") as f:
            lines = f.readlines()
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
                time.sleep(1)
            ToDelete = int(input("Enter the number for the log to delete: ")) -1
            del lines[ToDelete]
            print("\nupdated logs")
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
        with open(File, "w") as f:
            for line in lines:
                f.write(line)
        print("\n Log deleted \n")

    if Process == 4:
        with open(File, "w") as f:
            Entry = int(input("How much have you done you activity for (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            LineToWrite = f"{date_str} - {Entry} hours doing activity\n"
            f.write(LineToWrite)
            time.sleep(0.5)
            print("Log Rewritten\n")
            time.sleep(0.5)
    if Process == 5:
         with open(File, "r") as f:
            Search = input("Enter a date in form dd/mm/yy or hours doing activity to search for: ")
            lines = f.readlines()
            found = False
            if len(Search) == 8 and Search[2] == '/' and Search[5] == '/':
                for NewLine, line in enumerate(lines, 1):
                    if Search in line:
                        print(f"{NewLine}: {line.strip()}")
                        found = True
            else:
                target = f"{Search} hours doing activity"
                for NewLine, line in enumerate(lines, 1):
                    if target in line:
                        print(f"{NewLine}: {line.strip()}")
                        found = True
            if not found:
                print("No matching logs found.")

    if Process == 6:
        with open(File, "r") as f:
            period = input("Enter week, month, or year for timeframe: ").lower()
            lines = f.readlines()
            TotalHours = 0
            Entries = 0
            Now = datetime.datetime.now()
            CurrentWeek = Now.isocalendar()[1]
            CurrentMonth = Now.month
            CurrentYear = Now.year
            for line in lines:
                DateStr, Rest = line.split(" - ")
                EntryDate = datetime.datetime.strptime(DateStr, "%d/%m/%y")
                HourStr = Rest.split()[0]
                Hours = int(HourStr)
                if period == "week":
                    if EntryDate.isocalendar()[1] == CurrentWeek and EntryDate.year == CurrentYear:
                        TotalHours += Hours
                        Entries += 1
                elif period == "month":
                    if EntryDate.month == CurrentMonth and EntryDate.year == CurrentYear:
                        TotalHours += Hours
                        Entries += 1
                elif period == "year":
                    if EntryDate.year == CurrentYear:
                        TotalHours += Hours
                        Entries += 1
            if Entries > 0:
                print(f"Total hours doing activity : {TotalHours}")
                print(f"Average hours doing activity: {TotalHours / Entries:.2f}")
            else:
                print(f"No entries found for {period}")

while True:
    MainMenu()
    
    while True:
        try:
            TrackerChoice = int(input("Enter Assigned Number of Tracker to acess: "))
            if TrackerChoice <= 7 and TrackerChoice >= 1:
                break
            else:
                print("\nEnter number between 1 and 7")
                continue
        except ValueError:
            print("\nEnter valid integer")
            
    if TrackerChoice == 7:
        while True:
            try:
                leaving = int(input("\nDo you want to exit?\n yes(1)/no(2): "))
                if leaving == 1 or leaving == 2:
                    break
                else:
                    print("\nEnter values 1(yes) or 2(no)")
                    continue
            except ValueError:
                print("\nenter valid integer")
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
                print("\nEnter valid number between 1 and 6")
        except ValueError:
            print("\nEnter an Integer")
            
    FileManagement(TrackerChoice,ProcessChoice)
