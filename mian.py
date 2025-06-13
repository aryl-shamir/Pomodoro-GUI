# ---------------------------- IMPORTS ------------------------------- #
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Stops the current timer, resets the UI and repetition counter."""
    window.after_cancel(timer)
    time_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER START ------------------------------- #
def start_timer():
    """Starts the appropriate timer (work, short break, or long break) based on the repetition count."""
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        time_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        time_label.config(text="Short Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        time_label.config(text="Work Time", fg=GREEN)
        count_down(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Performs countdown every second and updates the timer display."""
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    else:
        seconds = str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# --- Tomato Image ---
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

# --- Timer Label ---
time_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
time_label.grid(column=1, row=0)

# --- Start Button ---
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# --- Reset Button ---
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# --- Check Label ---
check_label = Label(text="", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# --- Main loop ---
window.mainloop()
