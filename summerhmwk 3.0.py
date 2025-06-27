import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
window.minsize(500,500)
window.maxsize(500,500)
greeting = tk.Label(text="Sleep Tracking: (1)\nMood Tracking: (2)\nSpending Tracking: (3)\nBook Logs: (4)\nGame Tracking: (5)\nStudy Tracking: (6)\nExit: (7")
greeting.pack()
