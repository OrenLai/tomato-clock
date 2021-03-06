from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # stop the timer , reset the  timer text
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    # reset check mark
    check_mark_label.config(text="")
    # change the timer label
    title_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    reps += 1
    # expected behavior work(1) short_break(2) work(3) short_break work short_break work long_break

    if reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 1:  # round 1 3 5 7
        title_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)
    else:  # 2 4 6
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0 or count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    # change the data type of variable by changing the content in that variable is called dynamic typing
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer  # assign it to a variable so that we can stop it later with window.after_cancel method
        timer = window.after(1000, count_down, count - 1)
    else:  # if the count goes 0 , start another round of timer
        start_timer()
        #  update the check marks
        check_marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check_marks += "???"
        check_mark_label.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
# add padding to the image to place it in the middle
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# use PhotoImage class to create the pic object for canvas to use
tomato_img = PhotoImage(file="tomato.png")
# set the hightlightthickness to 0 to remove the white border around the picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

window.mainloop()
