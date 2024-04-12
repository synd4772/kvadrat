from dis import show_code
from tkinter import *
from tkinter import messagebox as mb
import math
import numpy as np
import matplotlib.pyplot as plt
global show_another
#+--------------------------------------------------------------------------------------------------+

def kala():
    x1 = np.arange(0, 9.5, 0.5)
    x2 = np.arange(-10, 0.5, 0.5)
    x3 = np.arange(-9, -2.5, 0.5)
    x4 = np.arange(-3, 9.5, 0.5)
    x5 = np.arange(5, 9, 0.5)
    x6 = np.arange(5, 8.5, 0.5)
    x7 = np.arange(-13, -8.5, 0.5)
    x8 = np.arange(-15, -12.5, 0.5)
    x9 = np.arange(-15, -10, 0.5)
    x10 = np.arange(3,4,0.5)

    y1= (2/27)*x1*x1-3
    y2= 0.04*x2*x2-3
    y3= (2/9)*(x3+6)**2+1
    y4= (-1/12)*(x4-3)**2+6
    y5= (1/9)*(x5-5)**2+2
    y6= (1/8)*(x6-7)**2+1.5
    y7= -0.75*(x7+11)**2+6
    y8= (-0.5)*(x8+13)**2+3
    y9= [1]*len(x9)
    y10= [3]*len(x10)

    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Kala")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
def prillid():
    x1 = np.arange(-9, -0.5, 0.5)
    x2 = np.arange(1, 9.5, 0.5)
    x3 = np.arange(-9, -0.5, 0.5)
    x4 = np.arange(1, 9.5, 0.5)
    x5 = np.arange(-9, -5.5, 0.5)
    x6 = np.arange(6, 9.5, 0.5)
    x7 = np.arange(-1, 1.5, 0.5)

    y1= (-1/16)*(x1+5)**2+2
    y2= (-1/16)*(x2-5)**2+2
    y3= (1/4)*(x3+5)**2-3
    y4= (1/4)*(x4-5)**2-3
    y5= -1*(x5+7)**2+5
    y6= -1*(x6-7)**2+5
    y7= -0.5*x7**2+1.5

    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("Kala")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
def zontik():
    x1 = np.arange(-12, 12.5, 0.5)
    x2 = np.arange(-4, 4.5, 0.5)
    x3 = np.arange(-12, -3.5, 0.5)
    x4 = np.arange(4, 12.5, 0.5)
    x5 = np.arange(-4, 0.5, 0.5)
    x6 = np.arange(-4, 0.7, 0.5)


    y1= (-1/18)*x1**2+12
    y2= (-1/8)*x2**2+6
    y3= (-1/8)*(x3+8)**2+6
    y4= (-1/8)*(x4-8)**2+6
    y5= 2*(x5+3)**2-9
    y6= 1.5*(x6+3)**2-10

    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Kala")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
func_list = [kala, prillid, zontik]
#
#+--------------------------------------------------------------------------------------------------+

def ShowAnother():
    global show_another
    print(show_another)
    if not show_another:
        t_button_f_frame['text'] = "Скрыть"
        root.geometry(f"{g_x}x{800}")
        s_frame.pack()
        R1.pack()
        R2.pack()
        R3.pack()
        show_another = True
    else:
        t_button_f_frame['text'] = "Раскрыть"
        root.geometry(f"{g_x}x{200}")
        s_frame.pack_forget()
        show_another = False
   

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
    print(show_another)
    if show_another:
        for index, i in enumerate(func_list):
            if index + 1 == int(var.get()):
                i()
    else:
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




#Default parameters
g_x = 1000
g_y = 200
default_font = ("Arial", 20)
default_bg = "blue"
default_fg = "green"

#Window config
root = Tk()
root.geometry(f"{g_x}x{g_y}")
root.resizable(False,True)

#----- MAIN ------

#Main Text
main_label = Label(root, text = "Решение квадратного уравнения", bg = default_bg, fg=default_fg, font = default_font)
main_label.pack()

#Calculation Frame
f_frame = Frame(root)

#Labels
label_list_text = ["x²+", "x+", "=", "0"]
label_list = list()
for index, i in enumerate(label_list_text):
    label_list.append(Label(f_frame, text = label_list_text[index]))
f_label_f_frame = label_list[0]
s_label_f_frame = label_list[1]
t_label_f_frame = label_list[2]
fo_label_f_frame = label_list[3]

#Entrys
entry_list = list()
for i in range(3):
    entry_list.append(Entry(f_frame, width = 10, bg = default_bg))
f_entry_f_frame = entry_list[0]
s_entry_f_frame = entry_list[1]
t_entry_f_frame = entry_list[2]

#Buttons
button_config = [[Calculate, "Решить"], [grafik, "График"], [ShowAnother, "Раскрыть"]]
buttons_list = list()
for index, i  in enumerate(button_config):
    buttons_list.append(Button(f_frame, text=button_config[index][1], bg = "green", fg = "black", activeforeground="black", disabledforeground="black", font = default_font,command = button_config[index][0]))
f_button_f_frame = buttons_list[0]
s_button_f_frame = buttons_list[1]
t_button_f_frame = buttons_list[2]

#Packing
f_frame_elements = [f_entry_f_frame, f_label_f_frame, s_entry_f_frame, s_label_f_frame, t_entry_f_frame, t_label_f_frame, fo_label_f_frame]
for element in f_frame_elements: 
    element.config(fg = default_fg, font = default_font)
    element.pack(side = "left")
f_button_f_frame.pack(side = "left")
s_button_f_frame.pack(side = "left")
t_button_f_frame.pack(side = "left")

f_frame.pack()

result_label_f_frame = Label(root, text="Решение", bg = "yellow", fg = "black", font = default_font)
result_label_f_frame.pack()



#----- Another ------
s_frame = Frame(root, width=200, height = 200)
show_another = True
var = IntVar()
R1 = Radiobutton(s_frame, text="kala", variable=var, value = 1)
R2 = Radiobutton(s_frame, text="prillid", variable=var, value = 2)
R3 = Radiobutton(s_frame, text="zontik", variable=var, value = 3 )


#Starting
root.mainloop()