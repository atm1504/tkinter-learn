from tkinter import *

root = Tk()

# -> show this number on click
count=0
def myClick():
    global count
    count += 1;
    myLabel = Label(root, text="Current count is: " + str(count))
    myLabel.pack()


myButton = Button(root, text="First Button", padx=10, pady=10, command=myClick, fg="#000000", bg="black")
myButton.pack()


root.mainloop()


## Command to create exe file
## pyinstaller --onefile --icon=/images/quality.ico buttons.py