from tkinter import *

win = Tk()
win.geometry("700x800+350+10")  




data = ""

def show(value):
    global data
    data += str(value)
    var.set(data)



def back():
    global data
    data = data[: -1]
    var.set(data)



def calculate():
    global data
    result = str(eval(data))            # whether the data is in string, eval will convert it into int
    var.set(result)


def clear():
    global data
    data = ""
    var.set(data)



# Black outer frame
calcFrame = Frame(win, bg="black", width=400, height=600)
calcFrame.pack(padx=100, pady=100)
calcFrame.pack_propagate(False)

# top gray frame
frame_left = Frame(calcFrame, bg="black", width=200)
frame_left.pack(side=TOP, fill=BOTH, expand=True)



var = StringVar()

entry_box = Entry(frame_left, textvariable = var, bg = "black", fg = "white", font=("Arial", 28), justify=RIGHT, borderwidth=0, highlightthickness=0 )
entry_box.pack(side = BOTTOM, ipadx = 190, ipady = 20)





# bottom pink frame
frame_right = Frame(calcFrame, bg="pink", width=200, height = 280)
frame_right.pack(side=BOTTOM, fill=BOTH, expand=True)
frame_right.pack_propagate(False)


# first strip
frame_first = Frame(frame_right, bg = "black", height = 50)
frame_first.pack(fill = X, ipady = 15)
frame_first.pack_propagate(False)

# second strip
frame_first1 = Frame(frame_right, bg = "black", height = 50)
frame_first1.pack(fill = X, ipady = 15)

# third strip
frame_first2 = Frame(frame_right, bg = "black", height = 50)
frame_first2.pack(fill = X, ipady = 15)

# fourth strip
frame_first3 = Frame(frame_right, bg = "black", height = 50)
frame_first3.pack(fill = X, ipady = 15)

# fifth strip
frame_first4 = Frame(frame_right, bg = "black", height = 50)
frame_first4.pack(fill = X, ipady = 15)





# first strip button
button1 = Button(frame_first, text = "AC", bg = "#4F4F4F", fg = "white", font = 30, command = lambda: clear())
button1.place(x = 8, y = 5, height = 75, width = 90)

button2 = Button(frame_first, text = "%", bg = "#4F4F4F", fg = "white", font = 30, command = lambda: show("%"))
button2.place(x = 110, y = 5, height = 75, width = 90)

button3 = Button(frame_first, text = "back", bg = "#4F4F4F", fg = "white", font = 10, command = back)
button3.place(x = 212, y = 5, height = 75, width = 90)

button4 = Button(frame_first, text = "/", bg = "#4F4F4F", fg = "white", font = 10, command = lambda: show("/"))
button4.place(x = 314, y = 5, height = 75, width = 85)





# second strip button
button5 = Button(frame_first1, text = "9", bg = "gray", fg = "white", font = 30, command = lambda: show(9))
button5.place(x = 8, y = 5, height = 75, width = 90)

button6 = Button(frame_first1, text = "8", bg = "gray", fg = "white", font = 30, command = lambda: show(8))
button6.place(x = 110, y = 5, height = 75, width = 90)

button7 = Button(frame_first1, text = "7", bg = "gray", fg = "white", font = 30, command = lambda: show(7))
button7.place(x = 212, y = 5, height = 75, width = 90)

button8 = Button(frame_first1, text = "X", bg = "#4F4F4F", fg = "white", font = 30, command = lambda: show("*"))
button8.place(x = 314, y = 5, height = 75, width = 85)




# third strip button
button9 = Button(frame_first2, text = "4", bg = "gray", fg = "white", font = 30, command = lambda: show(4))
button9.place(x = 8, y = 5, height = 75, width = 90)

button10 = Button(frame_first2, text = "5", bg = "gray", fg = "white", font = 30, command = lambda: show(5))
button10.place(x = 110, y = 5, height = 75, width = 90)

button11 = Button(frame_first2, text = "6", bg = "gray", fg = "white", font = 30, command = lambda: show(6))
button11.place(x = 212, y = 5, height = 75, width = 90)

button12 = Button(frame_first2, text = "-", bg = "#4F4F4F", fg = "white", font = 30, command = lambda: show("-"))
button12.place(x = 314, y = 5, height = 75, width = 85)




# fourth strip button
button13 = Button(frame_first3, text = "1", bg = "gray", fg = "white", font = 30, command = lambda: show(1))
button13.place(x = 8, y = 5, height = 75, width = 90)

button14 = Button(frame_first3, text = "2", bg = "gray", fg = "white", font = 30, command = lambda: show(2))
button14.place(x = 110, y = 5, height = 75, width = 90)

button15 = Button(frame_first3, text = "3", bg = "gray", fg = "white", font = 30, command = lambda: show(3))
button15.place(x = 212, y = 5, height = 75, width = 90)

button16 = Button(frame_first3, text = "+", bg = "#4F4F4F", fg = "white", font = 30, command = lambda: show("+"))
button16.place(x = 314, y = 5, height = 75, width = 85)




# fifth strip button
button17 = Button(frame_first4, text = "00", bg = "gray", fg = "white", font = 30, command = lambda: show("00"))
button17.place(x = 8, y = 5, height = 72, width = 90)

button18 = Button(frame_first4, text = "0", bg = "gray", fg = "white", font = 30, command = lambda: show(0))
button18.place(x = 110, y = 5, height = 72, width = 90)

button19 = Button(frame_first4, text = ".", bg = "gray", fg = "white", font = 30, command = lambda: show("."))
button19.place(x = 212, y = 5, height = 72, width = 90)

button19 = Button(frame_first4, text = "=", bg = "orange", fg = "white", font = 30, command = calculate)
button19.place(x = 314, y = 5, height = 72, width = 85)




win.mainloop()