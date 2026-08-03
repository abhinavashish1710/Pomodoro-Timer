from tkinter import *
from tkinter import messagebox

WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60

timer = None


def countdown(count):
    global timer

    minutes = count // 60
    seconds = count % 60

    timer_label.config(text=f"{minutes:02}:{seconds:02}")

    if count > 0:
        timer = root.after(1000, countdown, count - 1)
    else:
        messagebox.showinfo("Pomodoro", "Time's Up!")


def start_work():
    countdown(WORK_TIME)


def short_break():
    countdown(SHORT_BREAK)


def long_break():
    countdown(LONG_BREAK)


def reset():
    global timer

    if timer:
        root.after_cancel(timer)

    timer_label.config(text="25:00")


root = Tk()
root.title("Pomodoro Timer")
root.geometry("350x300")
root.resizable(False, False)

Label(
    root,
    text="Pomodoro Timer",
    font=("Arial", 20, "bold")
).pack(pady=15)

timer_label = Label(
    root,
    text="25:00",
    font=("Arial", 40, "bold"),
    fg="red"
)
timer_label.pack(pady=15)

Button(
    root,
    text="Start Work",
    width=20,
    command=start_work
).pack(pady=5)

Button(
    root,
    text="Short Break",
    width=20,
    command=short_break
).pack(pady=5)

Button(
    root,
    text="Long Break",
    width=20,
    command=long_break
).pack(pady=5)

Button(
    root,
    text="Reset",
    width=20,
    command=reset
).pack(pady=5)

root.mainloop()
