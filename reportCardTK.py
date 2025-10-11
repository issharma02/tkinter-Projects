from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror


win = Tk()

win.geometry("500x600")
win.config(bg = "gray")

win.title("Student Report Card Generator")
win.resizable(False, False)



name = StringVar()
hindi = IntVar()
english = IntVar()
science = IntVar()
maths = IntVar()
sst = IntVar()

def total():
    return hindi.get() + english.get() + science.get() + maths.get() + sst.get()

def percentage():
    return total() / 5


def division():
    per = percentage()

    if per > 85:
        return "First division" 
    elif per > 60 and per < 85:
        return "Second division"
    else:
        return "Fail"




def submit_button():
    showinfo(title = "Result",
             message = f"""
             "Student name: " {name.get()},
             "Total Marks" {total()},
             "percentage" {percentage()},
             "Division" {division()}
             """
            )
    

def reset_all():
    name.set("")
    hindi.set(0)
    english.set(0)
    science.set(0)
    maths.set(0)
    sst.set(0)


schoolname = Label(win, text = "ABC School", font = ("Comic Sans MS", 20), bg = "gray")
schoolname.pack()

labelText = Label(win, text = "Best Wishes to all the Students", bg = "gray", fg = "red")
labelText.pack()


studentname = Label(win, text = "Student name", bg = "gray", font = ("default_font", 12))
studentname.place(x = 5, y = 120)

studentnameEntry = Entry(win, textvariable = name)
studentnameEntry.place(x = 120, y = 120)

label2 = Label(win, text = "Subject Scores", font = ("Comic Sans MS", 20), bg = "gray")
label2.place(x = 150, y = 170)


# hindi
hindiMarks = Label(win, text = "Hindi", bg = "gray", font = ("default_font", 12))
hindiMarks.place(x = 5, y = 230)

hindiMarksEntry = Entry(win, textvariable = hindi)
hindiMarksEntry.place(x = 120, y = 230)



# english
englishMarks = Label(win, text = "English", bg = "gray", font = ("default_font", 12))
englishMarks.place(x = 5, y = 270)

englishMarksEntry = Entry(win, textvariable = english)
englishMarksEntry.place(x = 120, y = 270)



# science
scienceMarks = Label(win, text = "Science", bg = "gray", font = ("default_font", 12))
scienceMarks.place(x = 5, y = 320)

scienceMarksEntry = Entry(win, textvariable = science)
scienceMarksEntry.place(x = 120, y = 320)



# maths
mathsMarks = Label(win, text = "Maths", bg = "gray", font = ("default_font", 12))
mathsMarks.place(x = 5, y = 370)

mathsMarksEntry = Entry(win, textvariable = maths)
mathsMarksEntry.place(x = 120, y = 370)



# sst
sstMarks = Label(win, text = "Social Studies", bg = "gray", font = ("default_font", 12))
sstMarks.place(x = 5, y = 420)

sstMarksEntry = Entry(win, textvariable = sst)
sstMarksEntry.place(x = 120, y = 420)



button = Button(win, text = "Submit", command = submit_button)
button.place(x = 50, y = 480)


resetButton = Button(win, text = "Reset", command = reset_all)
resetButton.place(x= 150, y = 480)


win.mainloop()