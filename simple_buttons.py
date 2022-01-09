from tkinter import *

root = Tk()
root.title("copy paste buttons")
root.geometry("400x250")

def button_command():
    #print ("hello world")
    textUser= entry1.get()
    print(textUser)

def button_command_2():
    textUser=   entry1.get()  #getting the entry from the user in the field 
    entry2.delete(0, END)  #clear the field before use
    entry2.insert(0, textUser)  #


entry1 = Entry (root , width = 20)
entry2= Entry (root , width = 20)

#entry1. place(x=0,y=0)
#entry2.grid(row=3,   column= 1)

entry1.place(relx= 0.5 , rely= 0.15, anchor = CENTER)



button1 = Button(root , text = "button_Console", command = button_command)
button1.place(relx= 0.5 , rely= 0.25, anchor = CENTER)


entry2.place(relx= 0.5 , rely= 0.4, anchor = CENTER)


button2 = Button(root , text = "button_paste", command = button_command_2)
button2.place(relx= 0.5 , rely= 0.5, anchor = CENTER)

root.mainloop()
