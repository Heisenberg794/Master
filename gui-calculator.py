from tkinter import *
from tkinter.font import Font
root = Tk()
root.title("calc")
root.geometry("350x435+450+165")
root.resizable(False,False)

#functions
#==============================================================

def onclk(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

#==============================================================
    
def clrtxt():
    global operator
    operator = ""
    text_input.set(operator)


#==============================================================

def equlclk():
    global operator
    sol = str(eval(operator))
    text_input.set(sol)
    operator=""



#===============================================================
#btn1
def on_enter1(e):
    btn1.configure(bg = "#000")

def on_leave1(e):
    btn1.configure(bg = "#333")

#==============================================================

#btn2
def on_enter2(e):
    btn2.configure(bg = "#000")

def on_leave2(e):
    btn2.configure(bg = "#333")

#==============================================================

#btn3
def on_enter3(e):
    btn3.configure(bg = "#000")

def on_leave3(e):
    btn3.configure(bg = "#333")

#==============================================================

#btn4
def on_enter4(e):
    btn4.configure(bg = "#000")

def on_leave4(e):
    btn4.configure(bg = "#333")

#==============================================================

#btn5
def on_enter5(e):
    btn5.configure(bg = "#000")

def on_leave5(e):
    btn5.configure(bg = "#333")

#==============================================================

#btn6
def on_enter6(e):
    btn6.configure(bg = "#000")

def on_leave6(e):
    btn6.configure(bg = "#333")

#==============================================================

#btn7
def on_enter7(e):
    btn7.configure(bg = "#000")

def on_leave7(e):
    btn7.configure(bg = "#333")

#==============================================================

#btn8
def on_enter8(e):
    btn8.configure(bg = "#000")

def on_leave8(e):
    btn8.configure(bg = "#333")

#==============================================================

#btn9
def on_enter9(e):
    btn9.configure(bg = "#000")

def on_leave9(e):
    btn9.configure(bg = "#333")

#==============================================================

#btn0
def on_enter0(e):
    btn0.configure(bg = "#000")

def on_leave0(e):
    btn0.configure(bg = "#333")

#==============================================================

#btnadd
def on_enteradd(e):
    btnadd.configure(bg = "#000")

def on_leaveadd(e):
    btnadd.configure(bg = "#333")

#==============================================================

#btnsub
def on_entersub(e):
    btnsub.configure(bg = "#000")

def on_leavesub(e):
    btnsub.configure(bg = "#333")

#==============================================================

#btnequal
def on_entereql(e):
    btnequal.configure(bg = "#000")

def on_leaveeql(e):
    btnequal.configure(bg = "#333")

#==============================================================

#btnclr
def on_enterclr(e):
    btnclr.configure(bg = "#000")

def on_leaveclr(e):
    btnclr.configure(bg = "#333")

#==============================================================

#btndiv
def on_enterdiv(e):
    btndiv.configure(bg = "#000")

def on_leavediv(e):
    btndiv.configure(bg = "#333")

#==============================================================


#btnmul
def on_entermul(e):
    btnmul.configure(bg = "#000")

def on_leavemul(e):
    btnmul.configure(bg = "#333")


#==============================================================================    
operator=""
text_input = StringVar()

#==============================================================


ent = Entry(width = 35,justify="right", bg = "cyan", borderwidth=2, textvariable = text_input, font = Font(size = 13), relief = SUNKEN)

btn7 = Button(text = "7", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk(7))
btn7.bind("<Enter>", on_enter7)
btn7.bind("<Leave>", on_leave7)




btn4 = Button(text = "4", padx=25, pady=20, bg="#333", fg = "red", font = Font(size = 15), command = lambda: onclk(4))
btn4.bind("<Enter>", on_enter4)
btn4.bind("<Leave>", on_leave4)




btn1 = Button(text = "1", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk(1))
btn1.bind("<Enter>", on_enter1)
btn1.bind("<Leave>", on_leave1)




btn8 = Button(text = "8", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk(8))
btn8.bind("<Enter>", on_enter8)
btn8.bind("<Leave>", on_leave8)




btn5 = Button(text = "5", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk(5))
btn5.bind("<Enter>", on_enter5)
btn5.bind("<Leave>", on_leave5)




btn2 = Button(text = "2", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk(2))
btn2.bind("<Enter>", on_enter2)
btn2.bind("<Leave>", on_leave2)




btn9 = Button(text = "9", padx=25, pady=20, bg="#333", fg = "red", font = Font(size = 15), command = lambda: onclk(9))
btn9.bind("<Enter>", on_enter9)
btn9.bind("<Leave>", on_leave9)




btn6 = Button(text = "6", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk(6))
btn6.bind("<Enter>", on_enter6)
btn6.bind("<Leave>", on_leave6)




btn3 = Button(text = "3", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk(3))
btn3.bind("<Enter>", on_enter3)
btn3.bind("<Leave>", on_leave3)




btn0 = Button(text = "0", padx=25, pady=20, bg="#333", fg = "red", font = Font(size = 15), command = lambda: onclk(0))
btn0.bind("<Enter>", on_enter0)
btn0.bind("<Leave>", on_leave0)




btnadd = Button(text = "+", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk("+"))
btnadd.bind("<Enter>", on_enteradd)
btnadd.bind("<Leave>", on_leaveadd)




btnsub = Button(text = "-", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk("-"))
btnsub.bind("<Enter>", on_entersub)
btnsub.bind("<Leave>", on_leavesub)




btnequal = Button(text = "=", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = equlclk)
btnequal.bind("<Enter>", on_entereql)
btnequal.bind("<Leave>", on_leaveeql)




btnclr = Button(text = "C", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = clrtxt)
btnclr.bind("<Enter>", on_enterclr)
btnclr.bind("<Leave>", on_leaveclr)




btndiv = Button(text = "/", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk("/"))
btndiv.bind("<Enter>", on_enterdiv)
btndiv.bind("<Leave>", on_leavediv)




btnmul = Button(text = "*", padx=25, font = Font(size = 15), pady=20, bg="#333", fg = "red", command = lambda: onclk("*"))
btnmul.bind("<Enter>", on_entermul)
btnmul.bind("<Leave>", on_leavemul)



#============================================================================
#grid  
ent.grid(row=0, column=0, columnspan=4, padx = 12, pady=14)
btn7.grid(row=1, column=0, sticky = E, pady=8)
btn4.grid(row=2, column=0, sticky = E, pady=8)
btn1.grid(row=3, column=0, sticky = E, pady=8)
btn0.grid(row=4, column= 0, sticky = E, pady = 8)

btn8.grid(row=1, column=1, pady=8,padx=10)
btn5.grid(row=2, column=1, pady=8,padx=10)
btn2.grid(row=3, column=1, pady=8,padx=10)
btndiv.grid(row=4, column=1, pady=8,padx=10)

btn9.grid(row=1, column=2, sticky = W, pady=8)
btn6.grid(row=2, column=2, sticky = W, pady=8)
btn3.grid(row=3, column=2, sticky = W, pady=8)
btnmul.grid(row=4, column=2, sticky = W, pady=8)

btnclr.grid(row = 1, column = 3)
btnadd.grid(row = 2, column = 3)
btnsub.grid(row = 3, column = 3)
btnequal.grid(row = 4, column = 3)


root.mainloop()