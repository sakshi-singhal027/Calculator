# importing tkinter
import tkinter as tk

# let's see what is inside tkinter module
# print(dir(tk))

# let's create the base GUI
root = tk.Tk()

# lets define all the function below this
def insert7():
    
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='7')
    else:
        label.config(text=previous_value + '7')

def insert8():

    # let's fetch what's already written on the label
    previous_value = label.cget('text')

    # if previous value / already written text on label is 0
    if previous_value == '0':

        # replace 0 with the digit
        label.config(text='8')

    # if previous value / already written text on label is not 0
    else:

        # append the digit at the end
        label.config(text=previous_value + '8')

def insert9():
    
    previous_value = label.cget('text')
    if previous_value == '0':
        label.config(text='9')
    else:
        label.config(text=previous_value + '9')

def insert_multiply():
    
    previous_value = label.cget('text')
    if previous_value != '0':
        label.config(text=previous_value + '*')
        

def evaluation():

    expression = label.cget('text')
    result = eval(expression)
    label.config(text=result)

# GUI properties
root.geometry('320x465') # size change
root.resizable(width=False, height=False) # Fixed size
root.title('Calculator') # title change
root.iconbitmap('calculator icon.ico')
root.config(bg='#FFFDD0') # giving a background color to root gui

# Adding widgets now
# label widget to display text
label = tk.Label(root, text='0', bg='#FFFDD0', font=('Comic Sans MS', 35), anchor='e', padx=10)
label.pack(pady=(65, 10), fill='x')

# let's add a new container in root GUI
frame = tk.Frame(root, bg='#FFFDD0')
frame.pack(fill='both')

# buttons --> row 0 --> Percentage, CE, C, Delete
btn_percent = tk.Button(frame, text='%', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_ce = tk.Button(frame, text='CE', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_c = tk.Button(frame, text='C', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_delete = tk.Button(frame, text='DEL', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_percent.grid(row=0, column=0, padx=3, pady=3)
btn_ce.grid(row=0, column=1, padx=3, pady=3)
btn_c.grid(row=0, column=2, padx=3, pady=3)
btn_delete.grid(row=0, column=3, padx=3, pady=3)

# buttons --> row 1 --> 7,8,9,*
btn_7 = tk.Button(frame, text='7', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert7)
btn_8 = tk.Button(frame, text='8', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert8)
btn_9 = tk.Button(frame, text='9', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert9)
btn_x = tk.Button(frame, text='*', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9), command=insert_multiply)
btn_7.grid(row=1, column=0, padx=3, pady=3)
btn_8.grid(row=1, column=1, padx=3, pady=3)
btn_9.grid(row=1, column=2, padx=3, pady=3)
btn_x.grid(row=1, column=3, padx=3, pady=3)

# buttons --> row 2 --> 4,5,6,-
btn_4 = tk.Button(frame, text='4', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_5 = tk.Button(frame, text='5', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_6 = tk.Button(frame, text='6', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_minus = tk.Button(frame, text='-', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_4.grid(row=2, column=0, padx=3, pady=3)
btn_5.grid(row=2, column=1, padx=3, pady=3)
btn_6.grid(row=2, column=2, padx=3, pady=3)
btn_minus.grid(row=2, column=3, padx=3, pady=3)

# buttons --> row 3 --> 1,2,3,+
btn_1 = tk.Button(frame, text='1', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_2 = tk.Button(frame, text='2', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_3 = tk.Button(frame, text='3', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_plus = tk.Button(frame, text='+', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_1.grid(row=3, column=0, padx=3, pady=3)
btn_2.grid(row=3, column=1, padx=3, pady=3)
btn_3.grid(row=3, column=2, padx=3, pady=3)
btn_plus.grid(row=3, column=3, padx=3, pady=3)

# buttons --> row 4 --> +/-, 0, ., =
btn_divide = tk.Button(frame, text='/', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_0 = tk.Button(frame, text='0', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_decimal = tk.Button(frame, text='.', width=9, height=3, bg='#ffffff', relief='groove', font=('Trebuchet', 9))
btn_equal = tk.Button(frame, text='=', width=9, height=3, bg='#1e90ff', fg='#ffffff', relief='groove', font=('Trebuchet', 9), command=evaluation)
btn_divide.grid(row=4, column=3, padx=3, pady=3)
btn_0.grid(row=4, column=1, padx=3, pady=3)
btn_decimal.grid(row=4, column=2, padx=3, pady=3)
btn_equal.grid(row=4, column=0, padx=3, pady=3)


# let's run mainloop
root.mainloop()
