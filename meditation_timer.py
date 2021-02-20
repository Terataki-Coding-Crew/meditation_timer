from tkinter import *
import simpleaudio
from tkinter import ttk
import os.path
from math import floor
# from random import randint


# Constants
BLUE = "#99bbad"
PALE = "#ebd8b7"
MAUVE = "#c6a9a3"
LILAC = "#9a8194"
FONT_NAME = "Courier"
session_length = 0
phases = 0
ticks = 0
count_process = None

# Load images
image_list = []
path = "./images"
valid_images = [".png"]
for file in os.listdir(path):
    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue
    file = "images/" + file
    image_list.append(file)

print(image_list)

# Button functions

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(count_process)
    canvas.itemconfigure(timer_text, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global phases
    global image_list
    global ticks
    play_sound(beginning_bell)
    print(phases)
    for i in range(phases):
        count_down(ticks)
        if phases < phases:
            play_sound(phase_bell)
        phases -= 1
        # image_number = randint(0, len(image_list)-1)
        # selected_image = image_list[image_number]
        # print(selected_image)
        # print(type(selected_image))
        # new_image = PhotoImage(file=selected_image)
        # canvas.itemconfigure(centre_image, image=new_image)

    play_sound(end_bell)


# ---------------------------- PAUSE TIMER --------------------------------------- #
# def pause_timer():
#     window.after_idle()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # print(f"count: {count}")
    minutes = floor(count / 60)
    seconds = count % 60
    # print(f"seconds {seconds}")
    if seconds < 10:
        seconds = f"0{seconds}"
    count_text = f"{minutes}:{seconds}"
    canvas.itemconfigure(timer_text, text=count_text)
    if count > 0:
        global count_process
        count_process = window.after(1000, count_down, count - 1)  # Call count_down with count-1 as parameter
        # print(f"loop: {count}")
    # else:
    #     start_timer()


# Sounds
def play_sound(sound):
    sound.play()


beginning_bell = simpleaudio.WaveObject.from_wave_file("beginning_meditation_bell.wav")
phase_bell = simpleaudio.WaveObject.from_wave_file("phase_meditation_bell.wav")
end_bell = simpleaudio.WaveObject.from_wave_file("end_meditation_bell.wav")


# Selection
def get_selection():
    global session_length
    global phases
    global ticks
    session = combobox.get()
    choice = session.split()[0]
    if choice != 'Pick':
        session_length = int(choice) # Gets time as integer
        if session_length < 30:
            phases = int(session_length / 5)
            ticks = 300
        else:
            phases = int(session_length / 10)
            ticks = 600

# Layout

window = Tk()
window.title('Meditation Timer')
window.configure(bg=PALE, padx=89, pady=53)
title_label = Label(text= 'Meditation Timer', bg=PALE, fg=LILAC, font=(FONT_NAME, 23, 'bold'))
title_label.grid(row=0, column=1)
canvas = Canvas(width=300, height=400, bg=PALE)

# image = Image.open('ancient.png')
monk_image = PhotoImage(file='images/ancient.png')
centre_image = canvas.create_image(150, 200, image=monk_image) # Centre image
timer_text = canvas.create_text(150, 200, text="00:00", fill=PALE, font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

frame = Frame(window)
frame.configure(pady=10, bg=PALE)
frame.grid(column=1, row=2)


start_button = Button(frame, text='Start', bg=MAUVE, padx=40, command=start_timer)
# pause_button = Button(frame, text='Pause', bg=MAUVE, command=pause_timer)
end_button = Button(frame, text='End', bg=MAUVE, padx=40, command= reset_timer)
start_button.pack(side=LEFT)
# pause_button.pack()
end_button.pack(side=RIGHT)
select_label = Label(text= 'Please select session time:', padx= 10 ,bg=PALE, fg=LILAC, font=(FONT_NAME, 17, 'bold'))
select_label.grid(row=3, column=1, pady=10)

# Combobox
combo_frame = Frame()
combo_frame.configure(pady=10, bg=PALE)
combo_frame.grid(row=4, column=1, padx=10, pady=10)

options = ['10 minutes', '15 minutes', '20 minutes', '30 minutes', '60 minutes']
combobox = ttk.Combobox(combo_frame, values=options)
combobox.set('Pick a time')
combobox.pack(side=LEFT)
combo_button = Button(combo_frame, text="Choose", command=get_selection, bg=MAUVE)
combo_button.pack(side=RIGHT)


window.mainloop()
