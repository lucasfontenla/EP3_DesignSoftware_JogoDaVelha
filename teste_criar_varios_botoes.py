import tkinter as tk

window = tk.Tk()
number_of_buttons = 9
buttons = [0]*number_of_buttons

print(len(buttons))

for i in range(0, number_of_buttons):
    buttons[i] = tk.Button(window)
    buttons[i].pack()
    print(i)
    
window.mainloop()