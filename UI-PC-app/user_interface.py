import tkinter as tk
import buttons_functionality as butsf

#Initial window size
geometry_x = 920
geometry_y = 510

#Root configure
root = tk.Tk()
root.title('Stocks exchange helper')
root.geometry(f'{geometry_x}x{geometry_y}')
root.configure(bg='#121212')
root.minsize(geometry_x, geometry_y)
root.iconbitmap('icon.ico')

#Widget of state of program at each step of working
info = tk.StringVar()
Info_bar = tk.Label(root, textvariable=info, anchor='nw', font='TkSmallCaptionFont 9', bg='#1f1f1f', fg='#dbdadc')

#Top 10 text widget creation
top_10 = tk.StringVar()
top_10.set('No data provided')
Top_10_upper = tk.Label(root, text='TOP 10', anchor='center', font='Nexa\ Black 14', bg='#121212', fg='#066110', padx=16)
Top_10_bar = tk.Label(root, textvariable=top_10, anchor='nw', font='Nexa\ Light 12', bg='#2a2a2b', fg='#dbdadc')

#Bottom 10 text widget creation
bottom_10 = tk.StringVar()
bottom_10.set('No data provided')
Bottom_10_upper = tk.Label(root, text='WORST 10', anchor='center', font='Nexa\ Black 14', bg='#121212', fg='#6e0303')
Bottom_10_bar = tk.Label(root, textvariable=bottom_10, anchor='nw', font='Nexa\ Light 12', bg='#2a2a2b', fg='#dbdadc')

#Buttons widgets creation
Button_get_data = tk.Button(root, text='GET DATA', bd=0, font='Circular\ Std\ Medium 12', bg='#2a2a2b', fg='#dbdadc', activebackground='#727272', command=lambda: butsf.get_data(info, top_10, bottom_10), image = "1.png", compound=LEFT)
Button_send_data = tk.Button(root, state='disabled', text='SEND DATA', bd=0, font='Circular\ Std\ Medium 12', bg='#2a2a2b', fg='#dbdadc', activebackground='#727272', command=lambda: butsf.send_data(info))
Button_calculate = tk.Button(root, state='disabled', text='CALCULATE', bd=0, font='Circular\ Std\ Medium 12', bg='#2a2a2b', fg='#dbdadc', activebackground='#727272', command=lambda: butsf.calculate(info))
Button_top_10 = tk.Button(root, state='disabled', text='GET TOP 10', bd=0, font='Circular\ Std\ Medium 12', bg='#2a2a2b', fg='#dbdadc', activebackground='#727272', command=lambda: butsf.get_top_10(info, top_10))
Button_bottom_10 = tk.Button(root, state='disabled', text='GET WORST 10', bd=0, font='Circular\ Std\ Medium 12', bg='#2a2a2b', fg='#dbdadc', activebackground='#727272', command=lambda: butsf.get_bottom_10(info, bottom_10))


#Grid system configure
for i in range(5):
    root.rowconfigure(i, weight=1)

for i in range(3):
    root.columnconfigure(i, weight=1)


#Placing buttons in the root
Button_get_data.grid(row=0, column=0, padx=15, pady=15, sticky='nsew')
Button_send_data.grid(row=1, column=0, padx=15, sticky='nsew')
Button_calculate.grid(row=2, column=0, padx=15, pady=15, sticky='nsew')
Button_top_10.grid(row=3, column=0, padx=15, sticky='nsew')
Button_bottom_10.grid(row=4, column=0, padx=15, pady = 15, sticky='nsew')

#Placing Top 10 and Bottom 10 text widgets in the root
Top_10_upper.grid(row=0, column=1, padx=15, pady=15)
Top_10_bar.grid(row=1, column=1, rowspan=4, sticky='nsew', padx=15, pady=(0, 15))
Bottom_10_upper.grid(row=0, column=2, padx=15, pady=15)
Bottom_10_bar.grid(row=1, column=2, rowspan=4, sticky='nsew', padx=15, pady=(0, 15))

#Placing info text widget in the root
Info_bar.grid(row=5, column=0, columnspan=3, sticky='nsew')


#Binding functions and binding for buttons to light up when the cursor is on them and functions for blocking buttons if they cannot be used
def on_enter(event=None):
    if event.widget['state'] != 'disabled':
        event.widget['background'] = '#44414e'
    
    if butsf.send_data_state == 1:
        Button_send_data['state'] = 'normal'
    
    if butsf.calculate_state == 1:
        Button_calculate['state'] = 'normal'

    if butsf.get_top_10_state == 1:
        Button_top_10['state'] = 'normal'

    if butsf.get_bottom_10_state == 1:
        Button_bottom_10['state'] = 'normal'

    if butsf.send_data_state == 0:
        Button_send_data['state'] = 'disabled'
    
    if butsf.calculate_state == 0:
        Button_calculate['state'] = 'disabled'

    if butsf.get_top_10_state == 0:
        Button_top_10['state'] = 'disabled'
    
    if butsf.get_bottom_10_state == 0:
        Button_bottom_10['state'] = 'disabled'

def on_leave(event=None):
    event.widget['background'] = '#2a2a2b'

    if butsf.send_data_state == 1:
        Button_send_data['state'] = 'normal'

    if butsf.calculate_state == 1:
        Button_calculate['state'] = 'normal'

    if butsf.get_top_10_state == 1:
        Button_top_10['state'] = 'normal'

    if butsf.get_bottom_10_state == 1:
        Button_bottom_10['state'] = 'normal'

    if butsf.send_data_state == 0:
        Button_send_data['state'] = 'disabled'
    
    if butsf.calculate_state == 0:
        Button_calculate['state'] = 'disabled'

    if butsf.get_top_10_state == 0:
        Button_top_10['state'] = 'disabled'
    
    if butsf.get_bottom_10_state == 0:
        Button_bottom_10['state'] = 'disabled'


Button_get_data.bind("<Enter>", on_enter)
Button_get_data.bind("<Leave>", on_leave)
Button_send_data.bind("<Enter>", on_enter)
Button_send_data.bind("<Leave>", on_leave)
Button_calculate.bind("<Enter>", on_enter)
Button_calculate.bind("<Leave>", on_leave)
Button_top_10.bind("<Enter>", on_enter)
Button_top_10.bind("<Leave>", on_leave)
Button_bottom_10.bind("<Enter>", on_enter)
Button_bottom_10.bind("<Leave>", on_leave)


#Resizing of the text function and binding the text to resize if the app window is resizing
def font_resize(event=None):
    x = root.winfo_width()
    y = root.winfo_height()
    
    Top_10_upper.config(font=("Nexa Black", (int((x+y)/71.4))))
    Top_10_bar.config(font=("Nexa Light", (int((x+y)/93.3))))
    Bottom_10_upper.config(font=("Nexa Black", (int((x+y)/71.4))))
    Bottom_10_bar.config(font=("Nexa Light", (int((x+y)/93.3))))

    Button_get_data.config(font=("Circular Std Medium", (int((x+y)/87.3))))
    Button_send_data.config(font=("Circular Std Medium", (int((x+y)/87.3))))
    Button_calculate.config(font=("Circular Std Medium", (int((x+y)/87.3))))
    Button_top_10.config(font=("Circular Std Medium", (int((x+y)/87.3))))
    Button_bottom_10.config(font=("Circular Std Medium", (int((x+y)/87.3))))

    #Info_bar.config(font=("TkSmallCaptionFont", (int((x+y)/111.1))))

root.bind("<Configure>", font_resize)

root.mainloop()