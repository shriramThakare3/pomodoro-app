from tkinter import *
import math

# Constants
YELLOW = "#f7f5dd"
RED = "#e7305b"
PINK = "#e2979c"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_SEC = 4
LONG_BREAK_SEC = 15
reps = 0
timer = None

# Timer mechanism
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="green")
    check_mark.config(text="")

def start_timer():
    global reps, timer
    reps += 1
    work_min = WORK_MIN * 60
    short_break_sec =  SHORT_BREAK_SEC * 60
    long_break_sec = LONG_BREAK_SEC * 60
    if reps % 8 == 0:
        count_down(work_min)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(long_break_sec)
        title_label.config(text="Rest", fg=PINK)
    else:
        count_down(short_break_sec)
        title_label.config(text="Work", fg=GREEN)
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check_mark.config(text=mark)

# Countdown mechanism
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

# UI Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg="green", bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoimg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoimg)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg="green", bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
