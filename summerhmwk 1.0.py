import time
import datetime
import tkinter as tk

window = tk.Tk()
def MainMenu():
    print("\nSleep Tracking: (1)")
    print("Mood Tracking: (2)")
    print("Spending Tracking: (3)")
    print("Book Logs: (4)")
    print("Game Tracking: (5)")
    print("Study Tracking: (6)")
    print("Exit: (7)")

def Process():
    print("\nAppend: (1)")
    print("Read: (2)")
    print("Remove log: (3)")
    print("rewrite: (4)")
    print("Search: (5)")
    print("summary: (6)")    

def SleepTracking(x):
    if x == 1:
        with open("SleepTracking.txt", "a") as f:
            Entry = int(input("How many hours did you sleep (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - {Entry} hours of sleep\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 2:
        with open("SleepTracking.txt", "r") as f:
            for NewLine in f:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
    if x == 3:
        with open("SleepTracking.txt", "r") as f:
            lines = f.readlines()
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
                time.sleep(1)
            ToDelete = int(input("Enter the number for the log to delete: ")) -1
            del lines[ToDelete]
            print("\nupdated logs")
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
        with open("SleepTracking.txt", "w") as f:
            for line in lines:
                f.write(line)
        print("\n Log deleted \n")
    if x == 4:
        with open("SleepTracking.txt", "w") as f:
            Entry = int(input("How many hours did you sleep (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - {Entry} hours of sleep\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 5:
        with open("SleepTracking.txt", "r") as f:
            Search = input("Enter a date in form dd/mm/yy or hours slept to search for: ")
            lines = f.readlines()
            found = False
            if len(Search) == 8 and Search[2] == '/' and Search[5] == '/':
                for i, line in enumerate(lines, 1):
                    if Search in line:
                        print(f"{i}: {line.strip()}")
                        found = True
            else:
                for i, line in enumerate(lines, 1):
                    if f"{Search} hours" in line:
                        print(f"{i}: {line.strip()}")
                        found = True
            if not found:
                print("No matching logs found.")
    if x == 6:
        with open("SleepTracking.txt", "r") as f:
            lines = f.readlines()
            TotalHours = 0
            Entries = 0
            Now = datetime.datetime.now()
            CurrentWeek = Now.isocalendar()[1]
            CurrentMonth = Now.month
            CurrentYear = Now.year
            period = input("Enter week, month, or year for timeframe: ").lower()
            for line in lines:
                DateStr, Rest = line.split(" - ")
                EntryDate = datetime.datetime.strptime(DateStr, "%d/%m/%y")
                HourStr = Rest.split()[0]
                Hours = int(HourStr)
                if period == "week":
                    EntryWeek = EntryDate.isocalendar()[1]
                    if EntryWeek == CurrentWeek and EntryDate.year == CurrentYear:
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
                Average = TotalHours / Entries
                print(f"Total hours of sleep : {TotalHours}")
                print(f"Average hours of sleep: {Average:.2f}")
            else:
                print(f"No entries found for {period}")

def MoodTracking(x):
    if x == 1:
        with open("MoodTracking.txt", "a") as f:
            Entry = input("Describe your mood briefly: ")
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - Mood: {Entry}\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 2:
        with open("MoodTracking.txt", "r") as f:
            for NewLine in f:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
    if x == 3:
        with open("MoodTracking.txt", "r") as f:
            lines = f.readlines()
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
                time.sleep(1)
            ToDelete = int(input("Enter the number for the log to delete: ")) -1
            del lines[ToDelete]
            print("\nupdated logs")
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
        with open("MoodTracking.txt", "w") as f:
            for line in lines:
                f.write(line)
        print("\n Log deleted \n")
    if x == 4:
        with open("MoodTracking.txt", "w") as f:
            Entry = input("Describe your mood briefly: ")
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - Mood: {Entry}\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 5:
        with open("MoodTracking.txt", "r") as f:
            Search = input("Enter a date in form dd/mm/yy or a keyword to search for: ")
            lines = f.readlines()
            found = False
            if len(Search) == 8 and Search[2] == '/' and Search[5] == '/':
                for i, line in enumerate(lines, 1):
                    if Search in line:
                        print(f"{i}: {line.strip()}")
                        found = True
            else:
                for i, line in enumerate(lines, 1):
                    if Search.lower() in line.lower():
                        print(f"{i}: {line.strip()}")
                        found = True
            if not found:
                print("No matching logs found.")
    if x == 6:
        print("Summary not applicable for mood logs\n")

def SpendingTracking(x):
    if x == 1:
        with open("SpendingTracking.txt", "a") as f:
            Entry = float(input("How much did you spend: £"))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - £{Entry:.2f} spent\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 2:
        with open("SpendingTracking.txt", "r") as f:
            for NewLine in f:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
    if x == 3:
        with open("SpendingTracking.txt", "r") as f:
            lines = f.readlines()
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
                time.sleep(1)
            ToDelete = int(input("Enter the number for the log to delete: ")) -1
            del lines[ToDelete]
            print("\nupdated logs")
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
        with open("SpendingTracking.txt", "w") as f:
            for line in lines:
                f.write(line)
        print("\n Log deleted \n")
    if x == 4:
        with open("SpendingTracking.txt", "w") as f:
            Entry = float(input("How much did you spend: £"))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - £{Entry:.2f} spent\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 5:
        with open("SpendingTracking.txt", "r") as f:
            Search = input("Enter a date in form dd/mm/yy or amount spent to search for: ")
            lines = f.readlines()
            found = False
            if len(Search) == 8 and Search[2] == '/' and Search[5] == '/':
                for i, line in enumerate(lines, 1):
                    if Search in line:
                        print(f"{i}: {line.strip()}")
                        found = True
            else:
                target = f"£{Search}"
                for i, line in enumerate(lines, 1):
                    if target in line:
                        print(f"{i}: {line.strip()}")
                        found = True
            if not found:
                print("No matching logs found.")
    if x == 6:
        with open("SpendingTracking.txt", "r") as f:
            lines = f.readlines()
            Total = 0
            for line in lines:
                Amount = float(line.split("£")[1].split()[0])
                Total += Amount
            print(f"Total spent: £{Total:.2f}")
            if lines:
                print(f"Average per entry: £{Total / len(lines):.2f}")
            else:
                print("No entries to summarise.")

def BookLogs(x):
    if x == 1:
        with open("BookLogs.txt", "a") as f:
            Entry = input("Enter the book title and author: ")
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - {Entry}\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 2:
        with open("BookLogs.txt", "r") as f:
            for NewLine in f:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
    if x == 3:
        with open("BookLogs.txt", "r") as f:
            lines = f.readlines()
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
                time.sleep(1)
            ToDelete = int(input("Enter the number for the log to delete: ")) -1
            del lines[ToDelete]
            print("\nupdated logs")
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
        with open("BookLogs.txt", "w") as f:
            for line in lines:
                f.write(line)
        print("\n Log deleted \n")
    if x == 4:
        with open("BookLogs.txt", "w") as f:
            Entry = input("Enter the book title and author: ")
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            line_to_write = f"{date_str} - {Entry}\n"
            f.write(line_to_write)
            time.sleep(0.5)
            print("Log rewritten\n")
            time.sleep(0.5)
    if x == 5:
        with open("BookLogs.txt", "r") as f:
            Search = input("Enter a date in form dd/mm/yy or book details to search for: ")
            lines = f.readlines()
            found = False
            if len(Search) == 8 and Search[2] == '/' and Search[5] == '/':
                for i, line in enumerate(lines, 1):
                    if Search in line:
                        print(f"{i}: {line.strip()}")
                        found = True
            else:
                for i, line in enumerate(lines, 1):
                    if Search.lower() in line.lower():
                        print(f"{i}: {line.strip()}")
                        found = True
            if not found:
                print("No matching logs found.")
    if x == 6:
        with open("BookLogs.txt", "r") as f:
            lines = f.readlines()
            print(f"Total books logged: {len(lines)}")

def GameTracking(x):
    if x == 1:
        with open("GameTracking.txt", "a") as f:
            Entry = int(input("How much have you spent gaming (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            LineToWrite = f"{date_str} - {Entry} hours gaming\n"
            f.write(LineToWrite)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 2:
        with open("GameTracking.txt", "r") as f:
            for NewLine in f:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
    if x == 3:
        with open("GameTracking.txt", "r") as f:
            lines = f.readlines()
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
                time.sleep(1)
            ToDelete = int(input("Enter the number for the log to delete: ")) -1
            del lines[ToDelete]
            print("\nupdated logs")
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
        with open("GameTracking.txt", "w") as f:
            for line in lines:
                f.write(line)
        print("\n Log deleted \n")
    if x == 4:
        with open("GameTracking.txt", "w") as f:
            Entry = int(input("How much have you gamed for (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            LineToWrite = f"{date_str} - {Entry} hours gaming\n"
            f.write(LineToWrite)
            time.sleep(0.5)
            print("Log Rewritten\n")
            time.sleep(0.5)
    if x == 5:
        with open("GameTracking.txt", "r") as f:
            Search = input("Enter a date in form dd/mm/yy or hours gaming to search for: ")
            lines = f.readlines()
            found = False
            if len(Search) == 8 and Search[2] == '/' and Search[5] == '/':
                for NewLine, line in enumerate(lines, 1):
                    if Search in line:
                        print(f"{NewLine}: {line.strip()}")
                        found = True
            else:
                target = f"{Search} hours gaming"
                for NewLine, line in enumerate(lines, 1):
                    if target in line:
                        print(f"{NewLine}: {line.strip()}")
                        found = True
            if not found:
                print("No matching logs found.")
    if x == 6:
        with open("GameTracking.txt", "r") as f:
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
                print(f"Total hours gaming : {TotalHours}")
                print(f"Average hours gaming: {TotalHours / Entries:.2f}")
            else:
                print(f"No entries found for {period}")

def StudyTracking(x):
    if x == 1:
        with open("StudyTracking.txt", "a") as f:
            Entry = int(input("How much have you studied for (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            LineToWrite = f"{date_str} - {Entry} hours studying\n"
            f.write(LineToWrite)
            time.sleep(0.5)
            print("Entry added\n")
            time.sleep(0.5)
    if x == 2:
        with open("StudyTracking.txt", "r") as f:
            for NewLine in f:
                print(NewLine.strip())
                time.sleep(1)
            print("\n")
    if x == 3:
        with open("StudyTracking.txt", "r") as f:
            lines = f.readlines()
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
                time.sleep(1)
            ToDelete = int(input("Enter the number for the log to delete: ")) -1
            del lines[ToDelete]
            print("\nupdated logs")
            for NewLine, line in enumerate(lines):
                print(f"{NewLine + 1}: {line.strip()}")
        with open("StudyTracking.txt", "w") as f:
            for line in lines:
                f.write(line)
        print("\n Log deleted \n")
    if x == 4:
        with open("StudyTracking.txt", "w") as f:
            Entry = int(input("How much have you studied for (round to nearest hour): "))
            Now = datetime.datetime.now()
            date_str = Now.strftime("%d/%m/%y")
            LineToWrite = f"{date_str} - {Entry} hours studying\n"
            f.write(LineToWrite)
            time.sleep(0.5)
            print("Log Rewritten\n")
            time.sleep(0.5)
    if x == 5:
        with open("StudyTracking.txt", "r") as f:
            Search = input("Enter a date in form dd/mm/yy or hours studying to search for: ")
            lines = f.readlines()
            found = False
            if len(Search) == 8 and Search[2] == '/' and Search[5] == '/':
                for NewLine, line in enumerate(lines, 1):
                    if Search in line:
                        print(f"{NewLine}: {line.strip()}")
                        found = True
            else:
                target = f"{Search} hours studying"
                for NewLine, line in enumerate(lines, 1):
                    if target in line:
                        print(f"{NewLine}: {line.strip()}")
                        found = True
            if not found:
                print("No matching logs found.")
    if x == 6:
        with open("StudyTracking.txt", "r") as f:
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
                print(f"Total hours studying : {TotalHours}")
                print(f"Average hours studying: {TotalHours / Entries:.2f}")
            else:
                print(f"No entries found for {period}")

while True: #mainloop
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
