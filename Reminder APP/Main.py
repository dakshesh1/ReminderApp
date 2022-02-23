from tkinter import *
import time
from win10toast import ToastNotifier


def Reminder():
    noti = ToastNotifier()
    timee = int(innTime.get())
    work = innWORk.get()
    print("Done, You will be reminded")
    time.sleep(timee * 60)
    print("Hey,  you have to do the: ", work)
    noti.show_toast("Reminder", work, duration = 10)

def ReminerInhours():
    noti = ToastNotifier()
    timee = int(innTime.get())
    work = innWORk.get()
    print("Done, You will be reminded")
    time.sleep(timee * 3600)
    print("Hey,  you have to do the: ", work)
    noti.show_toast("Reminder", work, duration = 10)


    
def opp():
    if lblMorH.get() == "Minuites":
        Reminder()
    else:
        ReminerInhours()



window=Tk()
window.title('Reminder App')
window.geometry("300x200+100+100")

Titlee = Label(window, text="Reminer App", bg="Lime")
Titlee.pack(side=TOP)


lblt = Label(window, width=10, text=
"Time", bg="LightGreen")
lblt.pack(side=TOP)

innTime = Entry(window, bg="LightBlue", )
innTime.pack(side=TOP)

lbltorm = Label(window, text="Minuite/Hours", bg="Light Green")
lbltorm.pack(side=TOP)

lblMorH = Entry(window, bg="light blue")
lblMorH.pack(side=TOP)

lblw = Label(window, width=
10, text="WWhat is the work-", bg="LightGreen")
lblw.pack(side=TOP)

innWORk = Entry(window, bg="LightBlue")
innWORk.pack(side=TOP)

btn1 = Button(window, text="Click me", bg="LightBlue", command=opp)
btn1.pack(side=
BOTTOM)




window.configure(bg="Cyan")



window.mainloop()
