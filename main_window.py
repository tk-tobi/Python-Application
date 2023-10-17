import tkinter as tk 
from tkinter import ttk

# main window
main_window = tk.Tk()
main_window.title('Quick Mental Math')
main_window.geometry('900x500')

# print(ttk.Window().style.theme_names()) //check available theme names
'''
['cosmo', 'flatly', 'litera', 'minty', 'lumen', 'sandstone', 
'yeti', 'pulse', 'united', 'morph', 'journal', 'darkly', 
'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean']
'''

# Page Title
page_title = ttk.Label(master = main_window, text = "Mental Math")
page_title.pack()

# Page Widgets

    # Label
label = ttk.Label(master = main_window, text = 'Select Operation Category')
label.pack()

    # Selection Variable
select_var = tk.StringVar(value = "Select Operation")

    # Entry
operation = ttk.Entry(master = main_window, textvariable = select_var)
operation.pack()

    # Check Buttons
check_add = tk.IntVar(value = 0)
add_button = ttk.Checkbutton(master = main_window, 
                        text = '> Addition', 
                        command = lambda: select_var.set("Addition"),
                        variable = check_add)
add_button.pack()

check_sub = tk.IntVar(value = 0)
sub_button = ttk.Checkbutton(master = main_window, 
                        text = '> Subtraction',
                        command = lambda: select_var.set("Subtraction"),
                        variable = check_sub)
sub_button.pack()

check_mult = tk.IntVar(value = 0)
mult_button = ttk.Checkbutton(master = main_window, 
                         text = '> Multiplication',
                         command = lambda: select_var.set("Multiplication"),
                         variable = check_mult)
mult_button.pack()

check_div = tk.IntVar(value = 0)
div_button = ttk.Checkbutton(master = main_window, 
                        text = '> Division',
                        command = lambda: select_var.set("Division"),
                        variable = check_div)
div_button.pack()

check_conv = tk.IntVar(value = 0)
conv_button = ttk.Checkbutton(master = main_window, 
                         text = '> Conversion',
                         command = lambda: select_var.set("Conversion"),
                         variable = check_conv)
conv_button.pack()

check_perc = tk.IntVar(value = 0)
perc_button = ttk.Checkbutton(master = main_window, 
                         text = '> Percentage',
                         command = lambda: select_var.set('Percentage'),
                         variable = check_perc)
perc_button.pack()

check_derv = tk.IntVar(value = 0)
derv_button = ttk.Checkbutton(master = main_window, 
                         text = '> Derivatives',
                         command = lambda: select_var.set('Derivatives'),
                         variable = check_derv)
derv_button.pack()

check_intg = tk.IntVar(value = 0)
intg_button = ttk.Checkbutton(master = main_window, 
                         text = '> Integration',
                         command = lambda: select_var.set('Integration'),
                         variable = check_intg)
intg_button.pack()

check_lin = tk.IntVar(value = 0)
lin_button = ttk.Checkbutton(master = main_window, 
                        text = '> Linear Algebra',
                        command = lambda: select_var.set("Linear Algebra"),
                        onvalue = 1,
                        offvalue = 0,
                        variable = check_lin)
lin_button.pack()

# Select Mode
mode1 = ttk.Radiobutton(main_window,
                        value = 1,
                        text = 'Rapid fire [5 min]')
mode1.pack()

mode2 = ttk.Radiobutton(main_window,
                        value = 2,
                        text = 'Slow burn [15 min]')
mode2.pack()

mode3 = ttk.Radiobutton(main_window,
                        value = 3,
                        text = 'Endurance [30 mins]')
mode3.pack()

# run
main_window.mainloop()
