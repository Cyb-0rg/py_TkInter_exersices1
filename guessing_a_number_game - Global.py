from tkinter import *
import random 

root = Tk()
root.title("Generate a Random Number")
root.geometry("250x300")

frame = Frame (root)
 
def button_command():
 
    global magicNo1  #global for inter-functional usage
    magicNo1 = random.randint(1, 20)
    
    #entryHidden.delete(0, END)
    #entryHidden.insert(0, magicNo1)
    
    #print(magicNo)
    return magicNo1

def button_command_2( ):
    entryUser=   int( entry1.get() ) #getting the entry from the user in the field 
    entry2.delete(0, END)  #clear the field before use
    #magicNo = button_command()


    
    #magicNo= int ( entryHidden.get() )
    if (entryUser == magicNo1 ):
        entry2.insert(0, "correct")
    elif(entryUser  >  magicNo1 ):
        entry2.insert(0, "Try Smaller:")
    else:
        entry2.insert(0, "Try bigger:")
      



button1 = Button(root , text = "Generate a Random Number", command = button_command)
button1.place (relx= 0.5, rely= 0.18, anchor= CENTER)

label1  = Label(root, text= "Guess the Number in range 1-20")
label1.place (relx= 0.5, rely= 0.32, anchor= CENTER)


entry1 = Entry(root, width= 20, bg = "white")
entryHidden = Entry(root, width= 20,   bg = "#C7D8D9")


#entry2.grid(row=3,   column= 1)

entry1.place (relx= 0.5, rely= 0.4, anchor= CENTER)



button2 = Button(root , text = "Is It Correct?", command = button_command_2)
button2.place (relx= 0.5, rely= 0.72, anchor= CENTER)
 



entry2= Entry (root , width = 20)
entry2.place (relx= 0.5, rely= 0.8, anchor= CENTER)


 
root.mainloop()
