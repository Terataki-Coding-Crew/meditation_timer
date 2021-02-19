from tkinter import *
import simpleaudio
from tkinter import ttk
import os.path
from math import floor
from random import randint


# Constants
BLUE = "#99bbad"
PALE = "#ebd8b7"
MAUVE = "#c6a9a3"
LILAC = "#9a8194"
FONT_NAME = "Courier"
session_length = 0

# Load images
image_list = []
path = "./images"
valid_images = [".png"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    image_list.append(f)


print(image_list[0])


# Sounds
def play_sound(sound):
    play_obj = sound.play()
    play_obj.wait_done()

beginning_bell = simpleaudio.WaveObject.from_wave_file("beginning_meditation_bell.wav")
phase_bell = simpleaudio.WaveObject.from_wave_file("phase_meditation_bell.wav")
end_bell = simpleaudio.WaveObject.from_wave_file("end_meditation_bell.wav")


# Selection
def get_selection():
    global session_length
    session = combobox.get()
    choice = session.split()[0]
    if choice != 'Pick':
        session_length = (choice) # Gets time as integer
        print(session_length)





# Layout

window = Tk()
window.title('Meditation Timer')
window.configure(bg=PALE, padx=89, pady=53)
title_label = Label(text= 'Meditation Timer', bg=PALE, fg=LILAC, font=(FONT_NAME, 23, 'bold'))
title_label.grid(row=0, column=1)
canvas = Canvas(width=300, height=400, bg=PALE)

# image = Image.open('ancient.png')
monk_image = PhotoImage(file='images/ancient.png')
canvas.create_image(150, 200, image=monk_image) # Centre image
canvas.grid(row=1, column=1)

start_button = Button(text='Start', bg=MAUVE)
pause_button = Button(text='Pause', bg=MAUVE)
end_button = Button(text='End', bg=MAUVE)
start_button.grid(row=2, column=0)
pause_button.grid(row=2, column=1)
end_button.grid(row=2, column=2, pady= 10)
select_label = Label(text= 'Please select session time:', padx= 10 ,bg=PALE, fg=LILAC, font=(FONT_NAME, 17, 'bold'))
select_label.grid(row=3, column=1, pady=10)
options = ['10 minutes', '15 minutes', '20 minutes', '30 minutes']
combobox = ttk.Combobox(values=options)
combobox.set('Pick a time')
combobox.grid(row=4, column=1, padx=10, pady=10)
combo_button = Button(text = "Choose", command = get_selection, bg=MAUVE)
combo_button.grid(row=4, column=2, padx = 5, pady = 5)


window.mainloop()
