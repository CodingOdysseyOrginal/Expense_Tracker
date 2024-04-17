import tkinter as tk
from tkinter import ttk, messagebox

expenses = []

def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        expenses.append({'amount': amount, 'category': category})
        messagebox.showinfo('Info', 'Expense added successfully!')
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid amount.')

def print_expenses():
    expenses_text.delete(1.0, tk.END)
    for expense in expenses:
        expenses_text.insert(tk.END, f'Amount: {expense["amount"]:.2f}, Category: {expense["category"]}\n')

def total_expenses():
    total = sum(map(lambda expense: expense['amount'], expenses))
    messagebox.showinfo('Total Expenses', f'Total Expenses: ${total:.2f}')

def filter_expenses():
    category = filter_entry.get()
    filtered_expenses = filter(lambda expense: expense['category'] == category, expenses)
    expenses_text.delete(1.0, tk.END)
    for expense in filtered_expenses:
        expenses_text.insert(tk.END, f'Amount: {expense["amount"]:.2f}, Category: {expense["category"]}\n')

root = tk.Tk()
root.title('Expense Tracker')
root.configure(bg='#e6f7ff')

# Calculate screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 500
window_height = 700

x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)

root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), background='#99d6ff') 
style.configure('TLabel', font=('Arial', 12), background='#e6f7ff')  
style.configure('TEntry', font=('Arial', 12), background='#ccf2ff')  

amount_label = ttk.Label(root, text='Amount:')
amount_label.pack(pady=10)

amount_entry = ttk.Entry(root)
amount_entry.pack(pady=10)

category_label = ttk.Label(root, text='Category:')
category_label.pack(pady=10)

category_entry = ttk.Entry(root)
category_entry.pack(pady=10)

add_button = ttk.Button(root, text='Add Expense', command=add_expense)
add_button.pack(pady=10)

list_button = ttk.Button(root, text='List All Expenses', command=print_expenses)
list_button.pack(pady=10)

total_button = ttk.Button(root, text='Total Expenses', command=total_expenses)
total_button.pack(pady=10)

filter_label = ttk.Label(root, text='Filter by Category:')
filter_label.pack(pady=10)

filter_entry = ttk.Entry(root)
filter_entry.pack(pady=10)

filter_button = ttk.Button(root, text='Filter Expenses', command=filter_expenses)
filter_button.pack(pady=10)

expenses_text = tk.Text(root, height=10, width=50)
expenses_text.pack(pady=20)

root.mainloop()
