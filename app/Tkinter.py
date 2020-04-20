from tkinter import*
top=Tk()
top.geometry("600x300")
top.title("Ramudu")
count_Py=0
count_dj=0
count_Ra=0
total=0
def wish():
    global count_Py,total
    count_Py+=1
    L4.configure(text=count_Py)
    total+=3000
    L7.configure(text="Total Bill"+str(total))
def wish1():
    global count_dj,total
    count_dj+=1
    L5.configure(text=count_dj)
    total += 3000
    L7.configure(text="Total Bill" + str(total))
def wish2():
    global count_Ra,total
    count_Ra+=1
    L6.configure(text=count_Ra)
    total += 4500
    L7.configure(text="Total Bill" + str(total))


    #print("Hi Ram")
def dec_wish():
    global count_Py,total
    if count_Py>0:
        count_Py-=1
        L4.configure(text=count_Py)
        total-=3000
        L7.configure(text="Total" + str(total))


def dec_wish1():
    global count_dj,total
    if count_dj>0:
        count_dj-=1
        L5.configure(text=count_dj)
        total -= 3000
        L7.configure(text="Total" + str(total))

def dec_wish2():
    global count_Ra,total
    if count_Ra>0:
        count_Ra-=1
        L6.configure(text=count_Ra)
        total -= 3000
        L7.configure(text="Total" + str(total))


L1=Label(top,text="Python :3000")
L1.grid(row=0,column=0)
L2=Label(top,text="Django :3000")
L2.grid(row=1,column=0)
L3=Label(top,text="Restapi :3000")
L3.grid(row=2,column=0)
B1=Button(top,text="+",bg="Blue",fg="red",command=wish)
B1.grid(row=0,column=1)
B2=Button(top,text="+",bg="Blue",fg="red",command=wish1)
B2.grid(row=1,column=1)
B3=Button(top,text="+",bg="Blue",fg="red",command=wish2)
B3.grid(row=2,column=1)
L4=Label(top,text="0")
L4.grid(row=0,column=2)
L5=Label(top,text="0")
L5.grid(row=1,column=2)
L6=Label(top,text="0")
L6.grid(row=2,column=2)
B4=Button(top,text="-",bg="Blue",fg="red",command=dec_wish)
B4.grid(row=0,column=3)
B5=Button(top,text="-",bg="Blue",fg="red",command=dec_wish1)
B5.grid(row=1,column=3)
B6=Button(top,text="-",bg="Blue",fg="red",command=dec_wish2)
B6.grid(row=2,column=3)
L7=Label(top,text="Total 0.0")
L7.grid(row=4,column=0)
top.mainloop()