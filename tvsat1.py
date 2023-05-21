
import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime
channels =[
        "2  TVR 2 HD",
        "3  PRO TV HD",
        "4  Antena 1 HD",
        "5  Kanal D HD",
        "6  Prima TV HD",
        "7  Antena Stars HD",
        "8  Happy Channel HD", 
        "9  Moldova TV HD",
        "10 Prima Sport 1 HD",
        "11 Prima Sport 2 HD",
        "12 Prima Sport 3 HD",
        "13 Prima Sport 4 HD",
        "14 Eurosport 1 HD",
        "15 Eurosport 2 HD",
        "16 Pro Arena HD",
        "17 Romania TV",
        "18 Antena 3 HD",
        "19 Digi 24 HD",
        "20 Aleph News",
        "21 Realitatea Plus",
        "22 Cartoon Network",
        "23 Boomerang",
        "24 Disney Junior",
        "25 Disney Channel",
        "26 JimJam",
        "27 Minimax",
        "28 Nicktoons",
        "29 Nick Jr.",
        "30 Nickelodeon HD",
        "31 Discovery Channel",
        "32 Animal Planet HD",
        "33 Exploris HD",
        "34 Discovery Science HD",
        "35 Viasat Nature HD",
        "36 Viasat History HD",
        "37 History Channel HD",
        "38 Acasa TV HD",
        "39 Acasa Gold",
        "40 Pro Cinema",
        "41 Film Café",
        "42 DIVA",
        "43 TV1000",
        "44 Comedy Central",
        "45 AMC",
        "46 Bollywood HD",
        "47 AXN HD",
        "48 Warner TV",
        "49 FilmBox Extra HD",
        "50 ZU TV HD"
                ]




def save_results():
   
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    now = datetime.now()
    results_folder = os.path.join(desktop_path, now.strftime('%Y-%m-%d'))
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    file_name = now.strftime("%H-%M-%S") + '.txt'

    with open(os.path.join(results_folder, file_name), 'w', encoding='utf-8') as f:
        for channel in channels:
            f.write(channel + ' ' + channel_state[channel].get() + '\n')

root = tk.Tk()
root.title(" состояние каждого канала")

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side='left', fill='both', expand=True)

inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

scrollbar = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

canvas.configure(yscrollcommand=scrollbar.set)

channel_state = {}
for channel in channels:
    channel_state[channel] = tk.StringVar(value="соответствует")

for channel in channels:
    tk.Label(inner_frame, text=channel).grid(column=0, row=channels.index(channel))
    tk.Radiobutton(inner_frame, text="соответствует", variable=channel_state[channel], value="соответствует").grid(column=1, row=channels.index(channel))
    tk.Radiobutton(inner_frame, text="нет ЕПГ", variable=channel_state[channel], value="нет ЕПГ").grid(column=2, row=channels.index(channel))
    tk.Radiobutton(inner_frame, text="черный экран", variable=channel_state[channel], value="черный экран").grid(column=3, row=channels.index(channel))

save_button = tk.Button(root, text="Сохранить результаты", command=save_results)
save_button.pack()

root.mainloop()
