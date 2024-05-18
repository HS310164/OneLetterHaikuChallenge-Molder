import pyperclip
import re

import tkinter as tk
from tkinter import messagebox

def copy_clipboard(paticipants):
    paste = pyperclip.paste()

    paste_list = paste.replace('\r', '').replace('\n\n','\n').replace('\nスレ主\n','').split('\n')
    pattern = r'(20\d{2}/\d{2}/\d{2}|今日|昨日)\s\d{2}:\d{2}'

    str_list = []
    name_list = []
    haiku_list = []

    it = iter(paste_list)
    for tmp_name, tmp_str in zip(it, it):
        name = re.sub(pattern, "", tmp_name)
        str = tmp_str
        name_list.append(name[:-3])
        str_list.append(str)
        haiku_list.append([name, str])

    if not len(str_list) == 17:
        return 'A Length of This Haiku is not correct!!', ''

    haiku = [''.join(str_list[:5]), ''.join(str_list[5:12]), ''.join(str_list[12:])]
    haiku_text = haiku[0] + ' ' + haiku[1] + ' ' + haiku[2]
    if paticipants:
        pyperclip.copy(haiku_text + '\n参加者:\n' + ', '.join(name_list))
    else:
        pyperclip.copy(haiku_text)

    return haiku_text, '\n参加者:\n' + ', '.join(name_list)


def on_button_click(paticipants):
    haiku, names = copy_clipboard(paticipants)
    messagebox.showinfo("OneLetterHaikuChallenge-Molder", haiku + '\n' + names)


root = tk.Tk()
root.title("OneLetterHaikuChallenge-Molder")
root.geometry('200x120')
part_flag = tk.BooleanVar()
part_flag.set(False)

button = tk.Button(root, text="1文字俳句成形", command=lambda:on_button_click(part_flag.get()))
button.pack(pady=20)
part_check = tk.Checkbutton(root, text='参加者を含める', variable=part_flag)
part_check.place(x=20, y=50)

root.mainloop()
