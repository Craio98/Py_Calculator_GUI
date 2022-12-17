import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title("Calculator v1.01")
frame=tk.Frame(master=window,bg="#2f3133",padx=10)
frame.pack()
entry_mes = tk.Entry(master=frame, borderwidth=5, width=30)
entry_mes.grid(row=0, column=0, columnspan=8, ipady=1, pady=5)

#create function
def click_press(number):
    entry_mes.insert(tk.END, number)
 

def equal():
    try:
        y = str(eval(entry_mes.get()))
        entry_mes.delete(0, tk.END)
        entry_mes.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Check Syntax Error")
 
#After you hit the equal symbol, initial data will be replaced by the result
def clear():
    entry_mes.delete(0, tk.END)
 
 
button_1 = tk.Button(master=frame, text='1', bg="#303334",fg="white",padx=5,
                     pady=5, width=3, command=lambda: click_press(1))
button_1.grid(row=1, column=0, pady=1)
button_2 = tk.Button(master=frame, text='2', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(2))
button_2.grid(row=1, column=1, pady=1)
button_3 = tk.Button(master=frame, text='3', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(3))
button_3.grid(row=1, column=2, pady=1)
button_4 = tk.Button(master=frame, text='4', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(4))
button_4.grid(row=2, column=0, pady=1)
button_5 = tk.Button(master=frame, text='5', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(5))
button_5.grid(row=2, column=1, pady=1)
button_6 = tk.Button(master=frame, text='6', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(6))
button_6.grid(row=2, column=2, pady=1)
button_7 = tk.Button(master=frame, text='7', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(7))
button_7.grid(row=3, column=0, pady=1)
button_8 = tk.Button(master=frame, text='8', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(8))
button_8.grid(row=3, column=1, pady=1)
button_9 = tk.Button(master=frame, text='9', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(9))
button_9.grid(row=3, column=2, pady=1)
button_0 = tk.Button(master=frame, text='0', bg="#303334",fg="white", padx=5,
                     pady=5, width=3, command=lambda: click_press(0))
button_0.grid(row=4, column=1, pady=2)
 
button_add = tk.Button(master=frame, text="+", bg="#303334",fg="white", padx=15,
                       pady=5, width=3, command=lambda: click_press('+'))
button_add.grid(row=1, column=4, pady=2)
 
button_subtract = tk.Button(
    master=frame, text="-", padx=15, pady=5, width=3, bg="#303334",fg="white", 
    command=lambda: click_press('-'))
button_subtract.grid(row=2, column=4, pady=2)
 
button_multiply = tk.Button(
    master=frame, text="*", padx=15, pady=5, width=3, bg="#303334",fg="white", 
    command=lambda: click_press('*'))
button_multiply.grid(row=3, column=4, pady=2)
 
button_div = tk.Button(master=frame, text="/", padx=5, bg="#303334",fg="white",
                       pady=5, width=3, command=lambda: click_press('/'))
button_div.grid(row=4, column=4, pady=2)
 
button_clear = tk.Button(master=frame, text="Clear", bg="red",fg="white",
                         padx=15, pady=5, width=12, command=clear())
button_clear.grid(row=1, column=5, columnspan=2, pady=2)
 
button_equal = tk.Button(master=frame, text="=", bg="darkblue",fg="white", padx=5,
                         pady=5, width=9, command=equal)
button_equal.grid(row=2, column=5, columnspan=3, pady=2)

window.mainloop()

