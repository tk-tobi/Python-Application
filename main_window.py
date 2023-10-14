import tkinter as tk 
import ttkbootstrap as ttk

# main window
main_window = ttk.Window(themename = 'cosmo')
main_window.title("Journal Entry")
main_window.geometry("900x900")

# print(ttk.Window().style.theme_names()) //check available theme names
'''
['cosmo', 'flatly', 'litera', 'minty', 'lumen', 'sandstone', 
'yeti', 'pulse', 'united', 'morph', 'journal', 'darkly', 
'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean']
'''

# Page Title
page_title = ttk.Label(master = main_window, 
                       text = "Enter your journal entry for today",
                       font = 'Calibri 30 bold')
page_title.pack()


# run
main_window.mainloop()
