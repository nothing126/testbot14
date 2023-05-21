import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime

channels = [
    "1 Moldova 1",
    "2 Prime",
    "3 Canal 2",
    "4 Canal 3",
    "5 Publika TV",
    "6 Jurnal TV",
    "7 Primul în Moldova",
    "8 TV 8",
    "9 Moldova 2",
    "10 TVR Moldova",
    "11 N4",
    "12NTV Moldova",
    "13 RTR Moldova",
    "14 Exclusiv TV",
    "15 Mega TV",
    "16 Ren Moldova",
    "17 Canal 5",
    "18 TVC 21",
    "19 Сарафан",
    "20 Familia TV",
    "21 Тонус SD",
    "22 Cotidianul TV",
    "23 R live",
    "24 Privesc.EU TV",
    "25 Orhei TV",
    "26 RTVi",
    "27 Рен TV",
    "28 ITV",
    "29 Accent TV",
    "30 TV 6",
    "31 Elita TV",
    "32 SOR TV",
    "33 Studio L",
    "34 Drochia TV",
    "35 TV PRIM",
    "36 Media TV",
    "37 BTV",
    "38 NTS",
    "39 Legal TV",
    "40 STV",
    "41 TV-Gagauzia",
    "42 Orizont TV",
    "43 10 TV",
    "44 TV 1000",
    "45 TV 1000 Action",
    "46 Киносемья",
    "47 Кинохит",
    "48 Кинокомедия",
    "49 Мужсккое кино",
    "50Наше новое кино",
    "51 Родное Кино",
    "52 Paramount comedy",
    "53 Paramount channel",
    "54 Киноужас",
    "55 Filmbox",
    "56 Filmbox Artouse",
    "57 TimeLess Dizi Channel",
    "58 INSIGHN",
    "59 CTC Premier (cinema1)",
    "60 Zee TV",
    "61 Discovery Channel",
    "62 Discovery Science",
    "63 TLC",
    "64 Animal Planet",
    "65 Travel Channel",
    "66 Food Network",
    "67 Viasat Explorer",
    "68 Viasat History",
    "69 Моя Планета",
    "70 RT Documentary",
    "71 Приключения",
    "72 Живая Планета",
    "73 Наука 2.0",
    "74 Точка Отрыва",
    "75 Живая Природа",
    "76 DocuBox",
    "77 Интер +",
    "78 Мульт Bravo",
    "79 Nickelodeon",
    "80 Nick Jr.",
    "81 AXIAL TV",
    "82 Cartoon Network",
    "83 Boomerang",
    "84 Малыш",
    "85 Уникум",
    "86 Детский мир",
    "87 Nick Toons",
    "88 Gurinel TV",
    "89 Охота и рыбалка",
    "90 Дикий",
    "91 Дикая Охота",
    "92 Дикая рыбалка",
    "93 Охотник и рыбалов",
    "94 Усадьба",
    "95 Кухня ТВ",
    "96 Здоровое ТВ",
    "97 В мире Животных",
    "98 Travel + Adventure",
    "99 Первый Космический",
    "100 Рыжий",
    "101 Наша Сибирь",
    "102 Арсенал",
    "103 Мир Вокруг",
    "104 Загородный",
    "105 Драив",
    "106 365 Дней",
    "107 КВН ТВ",
    "108 Мир Увличений",
    "109 Мама",
    "110 Мужской",
    "111 Глазами Туриста",
    "112 Fast&FunBox",
    "113 Gametoon",
    "114 FashionBox",
    "115 360 TuneBox",
    "116 WORLD FASHION CHANNEL HD",
    "117 Шансон",
    "118 Ностальгия",
    "119 Russia Today",
    "120 Agro TV Moldova",
    "121 EuroSport 1",
    "122 EuroSport 2",
    "123 M1 Global",
    "124 КХЛ ТВ",
    "125 Q Sport",
    "126 Спортивный",
    "127 Motosport.ru",
    "128 Матч! Планета",
    "129 Бокс ТВ",
    "130 Спорт 1",
    "131 Живи ТВ",
    "132 FightBox",
    "133 Noroc TV",
    "134 Ru TV Moldova",
    "135 MTV European",
    "136 VH1 European",
    "137 THT Music",
    "138 Жара",
    "139 MTV 80",
    "140 MTV 90",
    "141 Popas TV",
    "142 Tezaur TV",
    "143 Zona M",
    "144 Taraf TV",
    "145 Busuioc TV",
    "146 Europa Plus TV",
    "147 Etno TV",
    "148 Speranța TV",
    "149 Alfa Omega",
    "150 CNL",
    "151 Trinitas TV",
    "152 1+1 International",
    "153 CNN International",
    "154 Credo",
    "155 TV5 Monde Europe",
    "156 Erox",
    "157 Eroxxx",
    "158 Telestar 1",
    "159 GN TV",
    "160 Orizont TV (Romania)",
    "161 Nasul TV",
    "162 Emi TV",
    "163 Kapital TV",
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
