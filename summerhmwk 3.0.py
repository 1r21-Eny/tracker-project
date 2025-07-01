import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("960x720")
root.configure(bg = '#171f18')

notebook = ttk.Notebook(root)
notebook.pack(fill = 'both', expand = True)

frame_main = tk.Frame(notebook, bg = '#171f18')
frame_second = tk.Frame(notebook, bg = '#171f18')

notebook.add(frame_main, text = 'Main Menu')
notebook.add(frame_second, text = 'SleepTracking')

canvas = tk.Canvas(frame_main, bg = '#171f18', highlightthickness = 0)
canvas.pack(fill = 'both', expand = True)

def create_rounded_rect(c, x1, y1, x2, y2, r=20, **kwargs):
    points = [x1+r,y1, x2-r,y1, x2,y1, x2,y1+r, x2,y2-r, x2,y2, x2-r,y2, x1+r,y2, x1,y2, x1,y2-r, x1,y1+r, x1,y1]
    return c.create_polygon(points, smooth = True, **kwargs)

create_rounded_rect(canvas, 270, 100, 690, 290, r=30, fill = '#eaece5',
                    outline = '#171f18', width = 2)

text = "Sleep Tracking: (1)\nWeather Logs: (2)\nSpending Tracking: (3)\nBook Logs: (4)\nLog In Tracking: (5)\nRevision Tracking: (6)\nExit: (7)"
canvas.create_text(480, 195, text= text,
                   font = ("Proxima Nova", 15),
                   fill = "#484b52", justify = 'center', anchor = 'center')

entry_frame = tk.Frame(frame_main, bg = '#eaece5', bd = 2, relief = 'groove')
entry_frame.place(relx = 0.5, y = 320, anchor = 'center', width = 300, height = 40)

entry = tk.Entry(entry_frame, font = ("Proxima Nova",15),
                 fg = '#484b52', bg = '#eaece5', bd = 0, justify = 'center')
entry.pack(fill='both', expand = True, padx = 5, pady = 5)

def submit_choice():
    choice = entry.get().strip()
    if choice in [str(i) for i in range(1,8)]:
        notebook.select(frame_second)
        label = tk.Label(frame_second, text = f"User selected option {choice}",
                         font = ("Proxima Nova", 20), bg = '#171f18', fg = '#eaece5')
        label.pack(expand = True)
    else:
        print("Invalid choice, please enter a number 1-7")

submit_btn = tk.Button(frame_main, text = "Submit", command = submit_choice,
                       font = ("Proxima Nova", 13), bg = '#eaece5',
                       fg = '#484b52', relief = 'groove', bd = 2)
submit_btn.place(relx = 0.5, y = 370, anchor = 'center', width = 100, height = 35)

root.mainloop()
