import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Initialize the main application window
root = tk.Tk()
root.title("WalletWise")
root.geometry("800x600")

# Global dictionary to store expenses
expenses = {
    "Housing": 0,
    "Food": 0,
    "Car": 0,
    "Entertainment": 0,
    "Insurance": 0,
    "Gas": 0,
    "Savings": 0,
}

# List to store transaction history
transactions = []

# Function to navigate to the Home frame
def show_home():
    home_frame.tkraise()


# Function to navigate to the Budget frame
def show_budget():
    update_pie_chart()
    budget_frame.tkraise()


# Function to add an expense
def add_expense():
    category = category_var.get()
    amount = amount_var.get()
    if category and amount:
        try:
            amount = float(amount)
            expenses[category] += amount
            transactions.append((category, amount))
            update_transaction_list()
            messagebox.showinfo("Success", f"Added ${amount} to {category}")
            amount_var.set("")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
    else:
        messagebox.showerror("Error", "Please fill out all fields")


# Function to update the pie chart
def update_pie_chart():
    labels = expenses.keys()
    sizes = expenses.values()
    fig.clear()
    ax = fig.add_subplot(111)
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        pctdistance=0.85,  # distance of the percentage text from the center
    )

    # Set properties of labels and autopct texts to improve readability
    for text in texts:
        text.set_fontsize(10)
        text.set_color("black")
    for autotext in autotexts:
        autotext.set_fontsize(8)
        autotext.set_color("white")

    # Draw a circle at the center to make it look like a donut chart
    centre_circle = plt.Circle((0, 0), 0.70, fc="white")
    fig.gca().add_artist(centre_circle)

    ax.axis("equal")
    canvas.draw()


# Function to update the transaction list
def update_transaction_list():
    transaction_listbox.delete(0, tk.END)
    for i, transaction in enumerate(transactions):
        transaction_listbox.insert(
            tk.END, f"{i + 1}. {transaction[0]}: ${transaction[1]:.2f}"
        )


# Function to edit an expense
def edit_expense():
    try:
        selected_index = transaction_listbox.curselection()[0]
        category, amount = transactions[selected_index]
        new_amount = simpledialog.askfloat(
            "Edit Expense", f"Edit amount for {category}:", initialvalue=amount
        )
        if new_amount is not None:
            expenses[category] -= amount
            expenses[category] += new_amount
            transactions[selected_index] = (category, new_amount)
            update_transaction_list()
            messagebox.showinfo("Success", "Expense updated successfully")
    except IndexError:
        messagebox.showerror("Error", "No transaction selected")


# Function to delete an expense
def delete_expense():
    try:
        selected_index = transaction_listbox.curselection()[0]
        category, amount = transactions[selected_index]
        expenses[category] -= amount
        del transactions[selected_index]
        update_transaction_list()
        messagebox.showinfo("Success", "Expense deleted successfully")
    except IndexError:
        messagebox.showerror("Error", "No transaction selected")


# Create a main frame to hold navigation buttons
main_frame = tk.Frame(root, bg="black", width=200)
main_frame.pack(side="left", fill="y")

# Create frames for Home and Budget
home_frame = tk.Frame(root, bg="white")
budget_frame = tk.Frame(root, bg="white")

for frame in (home_frame, budget_frame):
    frame.place(relx=0.25, rely=0, relwidth=0.75, relheight=1)

# Navigation buttons
button_width = 20

home_button = tk.Button(
    main_frame,
    text="Home",
    command=show_home,
    bg="orange",
    fg="white",
    width=button_width,
)
budget_button = tk.Button(
    main_frame,
    text="Budget",
    command=show_budget,
    bg="orange",
    fg="white",
    width=button_width,
)

home_button.pack(fill="x")
budget_button.pack(fill="x")

# Home frame content
tk.Label(
    home_frame, text="Home - Input Expenses", font=("Helvetica", 16), bg="white"
).pack(pady=20)

category_var = tk.StringVar()
amount_var = tk.StringVar()

tk.Label(home_frame, text="Category:", bg="white").pack(pady=5)
category_entry = ttk.Combobox(home_frame, textvariable=category_var)
category_entry["values"] = list(expenses.keys())
category_entry.pack(pady=5)

tk.Label(home_frame, text="Amount:", bg="white").pack(pady=5)
amount_entry = tk.Entry(home_frame, textvariable=amount_var)
amount_entry.pack(pady=5)

add_button = tk.Button(
    home_frame, text="Add Expense", command=add_expense, bg="green", fg="white"
)
add_button.pack(pady=20)

tk.Label(home_frame, text="Transactions:", bg="white").pack(pady=5)
transaction_listbox = tk.Listbox(home_frame)
transaction_listbox.pack(pady=5, fill=tk.BOTH, expand=True)

edit_button = tk.Button(
    home_frame, text="Edit Selected", command=edit_expense, bg="blue", fg="white"
)
edit_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = tk.Button(
    home_frame, text="Delete Selected", command=delete_expense, bg="red", fg="white"
)
delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Budget frame content
tk.Label(
    budget_frame, text="Budget - Monthly Budgeting", font=("Helvetica", 16), bg="white"
).pack(pady=20)

fig = plt.figure(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=budget_frame)
canvas.get_tk_widget().pack()

# Start the application with the Home frame
show_home()

# Run the Tkinter event loop
root.mainloop()
