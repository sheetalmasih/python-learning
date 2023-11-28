from tabnanny import check
from tkinter import*

root=Tk()
root.title("TIC-TAC-TOE")

x_wins=0
o_wins=0
x_turn=True
game_over=False

def new_game():
    global x_turn, game_over
    
    b1["text"] = ""
    b2["text"] = ""
    b3["text"] = ""
    b4["text"] = ""
    b5["text"] = ""
    b6["text"] = ""
    b7["text"] = ""
    b8["text"] = ""
    b9["text"] = ""
    
    b1["bg"] = "lightpurple"
    b2["bg"] = "lightpurple"
    b3["bg"] = "lightpurple"
    b4["bg"] = "lightpurple"
    b5["bg"] = "lightpurple"
    b6["bg"] = "lightpurple"
    b7["bg"] = "lightpurple"
    b8["bg"] = "lightpurple"
    b9["bg"] = "lightpurple"
    
    x_turn = True
    status_label["text"] = "X's Turn"
    game_over = False

new_game_button=Button(text='NEW GAME',command=new_game)
status_label=Label(text="X's Turn")
score_label=Label(text='X:{} O:{}'.format(x_wins, o_wins))

new_game_button.grid(row=0, column=0)
status_label.grid(row=0, column=1)
score_label.grid(row=0, column=2)

def check_game_status(x_turn):
    if(x_turn):
        check = "X"
    else:
        check = "O"
    #   row
    if (b1 ["text"] == b2["text"] == b3["text"] == check):
        return b1, b2, b3
    if (b4 ["text"] == b5["text"] == b6["text"] == check):
        return b4, b5, b6
    if (b7 ["text"] == b8["text"] == b9["text"] == check):
        return b7, b8, b9
    # colounm
    if (b1 ["text"] == b4["text"] == b7["text"] == check):
        return b1, b4, b7
    if (b2 ["text"] == b5["text"] == b8["text"] == check):
        return b2, b5, b8
    if (b3 ["text"] == b6["text"] == b9["text"] == check):
        return b1, b2, b3
    # dialoganls
    if (b1 ["text"] == b5["text"] == b9["text"] == check):
        return b1, b5, b9
    if (b3 ["text"] == b5["text"] == b7["text"] == check):
        return b3, b5, b7
    
    return None


def on_click(button):
    global x_turn, game_over, x_wins, o_wins
    if(button['text']!= "" or game_over):
        return
    button['text'] = "X" if x_turn else "O"
    b = check_game_status(x_turn)
    if(b !=None):
        b[0]["bg"] = "green"
        b[1]["bg"] = "green"
        b[2]["bg"] = "green"
        
        if(x_turn):
            status_label["text"] = "X wins"
            x_wins += 1
        else:
            status_label["text"] = "O wins"
            o_wins += 1
        score_label["text"] = "X:{} O:{}".format(x_wins, o_wins)
        game_over = True
        return
    x_turn = not x_turn
    status_label["text"] = "X's Turn" if x_turn else "O's Trun"
            

b1=Button(width=10, height=5, bg='pink', command=lambda: on_click(b1))
b2=Button(width=10, height=5, bg='pink', command=lambda: on_click(b2))
b3=Button(width=10, height=5, bg='pink', command=lambda: on_click(b3))
b4=Button(width=10, height=5, bg='pink', command=lambda: on_click(b4))
b5=Button(width=10, height=5, bg='pink', command=lambda: on_click(b5))
b6=Button(width=10, height=5, bg='pink', command=lambda: on_click(b6))
b7=Button(width=10, height=5, bg='pink', command=lambda: on_click(b7))
b8=Button(width=10, height=5, bg='pink', command=lambda: on_click(b8))
b9=Button(width=10, height=5, bg='pink', command=lambda: on_click(b9))

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

root.mainloop()