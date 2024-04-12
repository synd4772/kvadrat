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

def mainEx():
    first, second, third = GetAllEntrys()
    if ValuesCheck(first, second, third):
        if first == "" or second == "" or third == "":
            mb.showwarning("Tähelepanu!", "On vaja siseta üks sõna")
            return
        d = desc(first, second, third)
        f_x, s_x = find_x(d, first, second)

        result_label_f_frame.config(text = f"D = {d}\nx1 = {f_x}\nx2 = {s_x}")

def desc(first, second, third):
    return (float(second) ** 2.) - (4. * float(first) * float(third))

def find_x(d, first, second):
    if d < 0:
        return "net kornej", "net kornej"
    else:
        print(first, second)
        f_x_f = (float(second) * -1.) + math.isqrt(d) 
        print((float(second) * -1.), f_x_f, math.isqrt(4.))
        f_x_s = f_x_f / (2. * float(first))

        s_x_f = (float(second) * -1.) - math.isqrt(d)
        s_x_s = s_x_f / (2. * float(first))

    return f_x_s, s_x_s


def grafik():
    first, second, third = GetAllEntrys()
    if ValuesCheck(first, second, third):
        x0 = (-second) / (2 * first)
        y0 = first * x0 + second * x0 + third
        x1 = np.arange(x0-10., x0+10., 0.5)
        y1 = first * x1 * x1 + second * x1 + third
        fig = plt.figure()
        plt.plot(x1, y1, "r-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
  
#+--------------------------------------------------------------------------------------------------+
#+--------------------------------------------------------------------------------------------------+

default_font = ("Arial", 20)
default_bg = "blue"
default_fg = "green"

root = Tk()
root.geometry("700x400")

main_label = Label(root, text = "Решение квадратного уравнения", bg = default_bg, fg=default_fg, font = default_font)
main_label.pack()

f_frame = Frame(root)
f_label_f_frame = Label(f_frame, text = "x**2+")
s_label_f_frame = Label(f_frame, text = "x+")
t_label_f_frame = Label(f_frame, text = "=")
fo_label_f_frame = Label(f_frame, text = "0")

entry_list = list()
for i in range(3):
    entry_list.append(Entry(f_frame, width = 10, bg = default_bg))

f_entry_f_frame = entry_list[0]
s_entry_f_frame = entry_list[1]
t_entry_f_frame = entry_list[2]

f_button_f_frame = Button(f_frame, text="Решить", bg = "green", fg = "black", activeforeground="black", disabledforeground="black", font = default_font, command = mainEx) 
s_button_f_frame = Button(f_frame, text="График", bg = "green", fg = "black", activeforeground="black", disabledforeground="black", font = default_font, command= grafik) 

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