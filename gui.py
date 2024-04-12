from tkinter import *
from tkinter import messagebox as mb
import math
import numpy as np
import matplotlib.pyplot as plt

#+--------------------------------------------------------------------------------------------------+
#+--------------------------------------------------------------------------------------------------+

def GetAllEntrys():
    try:
        first = float(f_entry_f_frame.get())
        second = float(s_entry_f_frame.get())
        third = float(t_entry_f_frame.get())
    except:
        result_label_f_frame.config(text = f"Error Values")
        return "","",""
    return first, second, third
    
def ValuesCheck(*args):
    for i in args:
        if i == "":
            return False
    return True

def Calculate():
    first, second, third = GetAllEntrys()
    if ValuesCheck(first, second, third):
        d = GetDiscriminant(first, second, third)
        f_x, s_x = FindXY(d)

        result_label_f_frame.config(text = f"D = {int(d)},\nx1 = {f_x},\nx2 = {s_x}")
    else:
        mb.showwarning("Внимание", "Неправильные значение, проверьте нету ли пустых записей или букв в записях")

def GetDiscriminant(first, second, third):
    return (float(second) ** 2.) - (4. * float(first) * float(third))

def FindXY(d):
    first, second, third = GetAllEntrys()
    if d < 0:
        return "Нет корней", "Нет корней"
    else:
        f_x_f = (second * -1.) + math.sqrt(int(d)) 
        f_x_s = f_x_f / (2. * first)

        s_x_f = (second * -1.) - math.sqrt(int(d))
        s_x_s = float(s_x_f) / (2 * first)

    return round(f_x_s, 2), round(s_x_s, 2)


def grafik():
    first, second, third = GetAllEntrys()
    if ValuesCheck(first, second, third):
        x0 = (-second) / (2 * first)
        y0 = first * x0 + second * x0 + third
        x1 = np.arange(x0 - 10., x0 + 10., 0.5)
        y1 = first * x1 * x1 + second * x1 + third
        fig = plt.figure()
        plt.plot(x1, y1, "r-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
    else:
        mb.showwarning("Внимание", "Неправильные значение, проверьте нету ли пустых записей или букв в записях")
  
#+--------------------------------------------------------------------------------------------------+
#+--------------------------------------------------------------------------------------------------+

default_font = ("Arial", 20)
default_bg = "blue"
default_fg = "green"

root = Tk()
root.geometry("900x400")

main_label = Label(root, text = "Решение квадратного уравнения", bg = default_bg, fg=default_fg, font = default_font)
main_label.pack()

f_frame = Frame(root)
label_list_text = ["x²+", "x+", "=", "0"]
label_list = list()
for index, i in enumerate(label_list_text):
    label_list.append(Label(f_frame, text = label_list_text[index]))
f_label_f_frame = label_list[0]
s_label_f_frame = label_list[1]
t_label_f_frame = label_list[2]
fo_label_f_frame = label_list[3]

entry_list = list()
for i in range(3):
    entry_list.append(Entry(f_frame, width = 10, bg = default_bg))

f_entry_f_frame = entry_list[0]
s_entry_f_frame = entry_list[1]
t_entry_f_frame = entry_list[2]

button_config = [[Calculate, "Решить"], [grafik, "График"]]
buttons_list = list()

for index, i  in enumerate(button_config):
    buttons_list.append(Button(f_frame, text=button_config[index][1], bg = "green", fg = "black", activeforeground="black", disabledforeground="black", font = default_font,command = button_config[index][0]))

f_button_f_frame = buttons_list[0]
s_button_f_frame = buttons_list[1]

f_frame_elements = [f_entry_f_frame, f_label_f_frame, s_entry_f_frame, s_label_f_frame, t_entry_f_frame, t_label_f_frame, fo_label_f_frame]
for element in f_frame_elements: 
    element.config(fg = default_fg, font = default_font)
    element.pack(side = "left")
f_button_f_frame.pack(side = "left")
s_button_f_frame.pack(side = "left")

f_frame.pack()

result_label_f_frame = Label(root, text="Решение", bg = "yellow", fg = "black", font = default_font)
result_label_f_frame.pack()

root.mainloop()