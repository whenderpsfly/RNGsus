import random
from tkinter import *


master = Tk()
master.title("RNGsus")
master.minsize(width=500, height=500)



def getNumber():
    quit()


x = random.randint(1,11);    


button = Button(master, text="Close", command=getNumber)
button.pack()

label = Label(master,text= "Your random number is:")
label.pack()

label = Label(master,text=x)
label.pack()



master.mainloop()
