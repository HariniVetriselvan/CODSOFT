import tkinter as tk

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()
    entry.delete(len(current) - 1)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg='lightgray')  # Set background color

# Create entry widget
entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('<-', 4, 0)  # Backspace button
]

# Add buttons to the window
for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14))
    if text == '<-':  # Backspace button
        btn.config(command=backspace)
    else:
        btn.config(command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', width=5, height=2, font=('Arial', 14),
                      command=clear)
clear_btn.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

# Equal button
equal_btn = tk.Button(root, text='=', width=5, height=2, font=('Arial', 14),
                      command=calculate)
equal_btn.grid(row=5, column=2, columnspan=1, padx=5, pady=5)

root.mainloop()
