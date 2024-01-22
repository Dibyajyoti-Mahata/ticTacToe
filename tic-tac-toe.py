import tkinter as tk
from tkinter import messagebox
def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"]==buttons[combo[1]]["text"]==buttons[combo[2]]["text"]!="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("3T winner", f"player {buttons[combo[0]]['text']} wins")
            restart_game()
        
def button_click(index):
    if buttons[index]["text"]=="" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()
        check_draw()

def check_draw():
    global winner
    if all(button["text"] != "" for button in buttons)and all(button.cget("bg") == "yellow" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        winner = True
        restart_game()

def toggle_player():
    global current_player
    current_player = "x" if current_player=="0" else "0"
    label.config(text=f"player {current_player}'s turn")
def restart_game():
    global winner
    for button in buttons:
        button["text"] = ""
        button.config(bg="yellow")
    winner = False
    label.config(text=f"player {current_player}'s turn")
root=tk.Tk()
root.title("Tic-Tac-Toe")
buttons = [tk.Button(root, text="", font = ("normal",25), bg="yellow", fg = "red", width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)
current_player="x"
winner=False
label = tk.Label(root, text=f"player {current_player}'s turn", font =("normal", 16))
label.grid(row=3, column = 0, columnspan=3)
root.mainloop()
