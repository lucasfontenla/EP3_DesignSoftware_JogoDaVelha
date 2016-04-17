import tkinter as tk

def gera_botoes(top_level, numero_de_botoes):
    botoes = dict()
    
    for i in range(0, numero_de_botoes):
        botoes["Botão{0}".format(i)] = tk.Button(top_level)
        
    return botoes

window = tk.Tk()    

botoes = gera_botoes(window, 9)
    
for j in botoes.values():
    j.pack()    

window.mainloop()