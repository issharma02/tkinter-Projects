from tkinter import *

win = Tk()

fnameVar = StringVar()
lnameVar = StringVar()
mailVar = StringVar()
phoneVar = StringVar()
messageVar = StringVar()

def submit_all():
    print("First name: ", fnameVar.get())
    print("Last name: ", lnameVar.get())
    print("Mail: ", mailVar.get())
    print("Phone number: ", phoneVar.get())
    print("Message: ", message.get("1.0", END).strip())


win.geometry("1200x700")



winFrame = Frame(win, bg = "pink3")
winFrame.pack(expand = True, fill = BOTH)

formframe = Frame(winFrame, bg = "blue4", width = 1000, height = 550, relief = RAISED, bd = 2)
formframe.grid(row = 1, column = 1)

labelText = Label(formframe, text = "Just say Hello!", bg = "blue4", fg = "pink4", font = ("Arial", 25, "bold"))
labelText.grid(row = 1, column = 0)

labelText2 = Label(formframe, text = "Let us know more about you", bg = "blue4", fg = "white")
labelText2.grid(row = 2, column = 0)



homeLabel = Label(formframe, text = "HOME", bg = "blue4", fg = "white")
homeLabel.grid(row = 0, column = 1)

blogLabel = Label(formframe, text = "BLOG", bg = "blue4", fg = "white")
blogLabel.grid(row = 0, column = 2)

aboutLabel = Label(formframe, text = "ABOUT", bg = "blue4", fg = "white")
aboutLabel.grid(row = 0, column = 3)

contactLabel = Label(formframe, text = "CONTACT", bg = "blue4", fg = "white")
contactLabel.grid(row = 0, column = 4)




# textLabel = Label(formframe, text = "Just Say Hello! ")
# textLabel1 = Label(formframe, text = "Let us know more about you.")
# textLabel.grid(row = 1, column = 0, columnspan = 2)
# textLabel1.grid(row = 2, column = 0, columnspan = 2)


formfieldsFrame = Frame(formframe, bg = "blue4")
formfieldsFrame.grid(row=3, column=0, columnspan=4, pady=20, sticky = NSEW)



innerFrame = Frame(formfieldsFrame, bg = "blue4")
innerFrame.grid(row = 0, column = 0)



firstmname = Entry(innerFrame, textvariable = fnameVar, bg = "gray")
firstmname.grid(row = 0, column = 0, padx = 5, pady = 5, ipady = 8)

lastmname = Entry(innerFrame, textvariable = lnameVar, bg = "gray")
lastmname.grid(row = 0, column = 1, padx = 5, pady = 5, ipady = 8)

mail = Entry(innerFrame, textvariable = mailVar, bg = "gray")
mail.grid(row = 1, column = 0, padx = 5, pady = 5, ipady = 8)

phone = Entry(innerFrame, textvariable = phoneVar, bg = "gray")
phone.grid(row = 1, column = 1, padx = 5, pady = 5, ipady = 8)


message = Text(innerFrame, height = 5, width = 40, bg = "gray")
message.grid(row = 2, column = 0, columnspan = 2, sticky = W, padx = 30, pady = 10)







winFrame.columnconfigure(0, weight = 1)
winFrame.columnconfigure(1, weight = 1)
winFrame.columnconfigure(2, weight = 1)
winFrame.columnconfigure(3, weight = 1)
winFrame.columnconfigure(4, weight = 1)


winFrame.rowconfigure(0, weight = 1)
winFrame.rowconfigure(1, weight = 1)
winFrame.rowconfigure(2, weight = 1)
winFrame.rowconfigure(3, weight = 1)
winFrame.rowconfigure(4, weight = 1)
winFrame.rowconfigure(5, weight = 1)



formframe.columnconfigure(0, weight = 1)
formframe.columnconfigure(1, weight = 1)
formframe.columnconfigure(2, weight = 1)
formframe.columnconfigure(3, weight = 1)
formframe.columnconfigure(4, weight = 1)


formframe.rowconfigure(0, weight = 1)
formframe.rowconfigure(1, weight = 1)
formframe.rowconfigure(2, weight = 1)
formframe.rowconfigure(3, weight = 1)
formframe.rowconfigure(4, weight = 1)
formframe.rowconfigure(5, weight = 1)


formframe.grid_propagate(0)


# submit button
submit = Button(innerFrame, text = "Submit", command = submit_all)
submit.grid(row = 3, column = 0, padx = 10, pady = 10)



win.mainloop()