from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0

    # timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    #
    # title_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    frequency = 400
    duration = 1000
    winsound.Beep(frequency, duration)


    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps % 9 == 0:
        reps = 1
        checkmark_label.grid_forget()
    if reps % 8 == 0:
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        count_down(long_break_sec)
        title_text.config(text="Break", fg=RED)
        checkmark_label.config(text=f"✔" * int(reps / 2))
        print(reps)
    elif reps % 2 == 0:
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        if reps == 2:
            checkmark_label.grid(column=1, row=3)
        count_down(short_break_sec)
        title_text.config(text="Break", fg=PINK)
        checkmark_label.config(text=f"✔" * int(reps / 2))

        print(reps)
    else:
        winsound.Beep(1000, duration)
        winsound.Beep(1000, duration)
        count_down(work_sec)
        title_text.config(text="Work", fg=GREEN)
        print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    minute_text = math.floor(count / 60)
    seconds_text = count % 60


    if len(str(seconds_text)) == 1:
        seconds_text = "0" + str(seconds_text)

    # ANGELA'S SOLUTION
    # if seconds_text < 10:
    #   seconds_text = f"0{seconds_text}

    canvas.itemconfig(timer_text, text=f"{minute_text}:{seconds_text}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
#x and y position of the image in the window ^
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_text.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text="✔", bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)
checkmark_label.grid_forget()


window.mainloop()
