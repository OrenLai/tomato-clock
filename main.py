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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
# add padding to the image to place it in the middle
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# use PhotoImage class to create the pic object for canvas to use
tomato_img = PhotoImage(file="tomato.png")
# set the hightlightthickness to 0 to remove the white border around the picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset")
button_reset.grid(row=2, column=2)
check_mark = "✔"
check_mark_label = Label(text=f"{check_mark}", fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

window.mainloop()
