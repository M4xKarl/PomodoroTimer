import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BUTTON_FONT = FONT_NAME, 14, "bold"
reps = 0
TICK = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global timer
    global TICK
    global reps
    window.after_cancel(timer)
    TICK = ""
    reps = 0
    tick_label.config(text=TICK)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    reps += 1
    match reps:
        case 1:
            title_label.config(text="Work")
            count_down(25 * 60)
        case 2:
            title_label.config(text="Break")
            count_down(5 * 60)
        case 3:
            title_label.config(text="Work")
            count_down(25 * 60)
        case 4:
            title_label.config(text="Break")
            count_down(5 * 60)
        case 5:
            title_label.config(text="Work")
            count_down(25 * 60)
        case 6:
            title_label.config(text="Break")
            count_down(5 * 60)
        case 7:
            title_label.config(text="Work")
            count_down(25 * 60)
        case 8:
            title_label.config(text="Break")
            count_down(20 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor((count / 60))
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    if count == 0:
        global TICK
        TICK = TICK + "✔"
        tick_label.config(text=TICK)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Buttons

start_button = Button(text="Start", font=BUTTON_FONT, command=start_timer)
start_button.grid(column=0, row=2, sticky="w")
start_button.config(width=8)

reset_button = Button(text="Reset", font=BUTTON_FONT, command=reset)
reset_button.grid(column=2, row=2, sticky="w")
reset_button.config(width=8)

# Label

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.config(pady=10, padx=10)
title_label.grid(column=1, row=0)

tick_label = Label(text=TICK, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "normal"))
tick_label.config(pady=20, padx=5)
tick_label.grid(column=1, row=3)

window.mainloop()
