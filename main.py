from tkinter import *
count=0
board=[['','',''],['','',''],['','','']]
def TicTacToeGUI():
    #CODE OF GUI
    global t
    t=Tk()
    t.title("TIC-TAC-TOE")
    t.configure(bg="NavajoWhite2")
    player_turn_label=Label(t,text="Player:1(X)",height=2,font=('ArialBlack',14,"italic"),bg="NavajoWhite2",fg="black")
    player_turn_label.grid(row=0,column=0)
    restart_button=Button(t,text="RESTART",font=("@MalgunGothic",11,"underline"),bg="PaleVioletRed",fg="Black")
    restart_button.grid(row=0,column=2)
    g1=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g2=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g3=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g4=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g5=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g6=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g7=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g8=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g9=Button(t,text="",height=4,width=8,bg="aquamarine4",activebackground="Purple4",fg="White",font="BookmanOldStyle")
    g1.grid(row=2,column=0)
    g2.grid(row=2,column=1)
    g3.grid(row=2,column=2)
    g4.grid(row=3,column=0)
    g5.grid(row=3,column=1)
    g6.grid(row=3,column=2)
    g7.grid(row=4,column=0)
    g8.grid(row=4,column=1)
    g9.grid(row=4,column=2)
TicTacToeGUI()