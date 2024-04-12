
from tkinter import *
from tkinter import messagebox as mb
import math
import numpy as np
import matplotlib.pyplot as plt

def mainEx():
    
    first = f_entry_f_frame.get()
    second = s_entry_f_frame.get()
    third = t_entry_f_frame.get()
    if first == "" or second == "" or third == "":
        mb.showwarning("Tähelepanu!", "On vaja siseta üks sõna")
        return
    d = desc(first, second, third)
    f_x, s_x = find_x(d, first, second)

    result_label_f_frame.config(text = f"D = {d}\nx1 = {f_x}\nx2 = {s_x}")

def desc(first, second, third):
    
    y = (int(second) ** 2) - (4 *  int(first) * int(third))
    return y

def func(x):
    return 2.*x

# Значение интеграла, найденного аналитически, точно
def func_integr(x):
        return x**2.
def find_x(d, first, second):
    if d < 0:
        return "net kornej", "net kornej"
    else:
        print(first, second)
        f_x_f = (int(second) * -1) + math.isqrt(d) 
        print((int(second) * -1), f_x_f, math.isqrt(4))
        f_x_s = f_x_f / (2 * int(first))

        s_x_f = (int(second) * -1) - math.isqrt(d)
        s_x_s = s_x_f / (2 * int(first))

    return f_x_s, s_x_s


def grafik():
    first = int(f_entry_f_frame.get())
    second = int(s_entry_f_frame.get())
    third = int(t_entry_f_frame.get())

    # Диапазон изменения переменной по оси X
    x = np.linspace(-100, 100, 1000)
    y = first*x**2 + second*x + third  
 
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

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

f_entry_f_frame = Entry(f_frame, width = 10, bg = default_bg)
s_entry_f_frame = Entry(f_frame, width = 10, bg = default_bg)
t_entry_f_frame = Entry(f_frame, width = 10, bg = default_bg)

f_button_f_frame = Button(f_frame, text="Решить", bg = "green", fg = "black", activeforeground="black", disabledforeground="black", font = default_font, command = mainEx) 
s_button_f_frame = Button(f_frame, text="График", bg = "green", fg = "black", activeforeground="black", disabledforeground="black", font = default_font, command=grafik) 




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