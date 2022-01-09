from tkinter import *

def Calculate( ):

    oran = float (userInput1.get() )
    kidem = float (userInput2.get() )
    maas = float (userInput3.get() )

    zamli = maas * (1+ (kidem + oran)/100)
    zamli= format (zamli , ".2f")
    
    userInput4.delete(0, END)
    userInput4.insert(0, "$"+str(zamli))
     

 
ws = Tk()
ws.title("Wage Calculater")
ws.geometry("400x250")
 

frame = Frame(ws )

label1= Label(ws,text="Enter Wage Amount, Raise Rate and years of experience", font="Roboto 10", bg="#e1e3e2", fg="black",width=45, bd=2)
#label1.place(x=15,y=0)
#label1.grid(row = 0, column = 1)
label1.place(relx= 0.55, rely= 0.12, anchor= CENTER)

userInput1 = Entry(frame, width=30, justify= LEFT , bg="#FFFFFF")
userInput1.grid(row=2, columnspan=2, column= 1)

userInput2 = Entry(frame, width=30, justify= LEFT , bg="#FFFFFF")
userInput2.grid(row=3, columnspan=2, column= 1)

userInput3 = Entry(frame, width=30, justify= LEFT , bg="#FFFFFF")
userInput3.grid(row=4, columnspan=2, column= 1)

userInput4 = Entry(frame, width=30, justify= LEFT , bg="#FFFFFF")
userInput4.grid(row=5, columnspan=2, column= 1)




label2= Label(frame,text="Annual Raise Rate "  , width= 20  )
label2.grid(row = 2, column = 0)
 
label3= Label(frame,text="Years of Experince "  , width= 20 )
label3.grid(row =3, column = 0)

label4= Label(frame,text=" Current Wage "    , width= 20 )
label4.grid(row = 4, column = 0)

label5= Label(frame,text=" New Wage  = "    , width= 20)
label5.grid(row = 5, column = 0)


 
button= Button(frame,text="Calculate",command=Calculate, justify= RIGHT)
button.grid(row=6, column=1)


frame.place(relx= 0.5, rely= 0.48, anchor= CENTER)
ws.mainloop()
