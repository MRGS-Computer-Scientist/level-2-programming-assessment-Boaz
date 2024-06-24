from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from os import path
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1440x1024")
        self.window.title("WalletWise")

        self.current_frame = None

        self.create_widgets()
        self.show_home()  # Show the home frame initially
        self.window.mainloop()

    def create_widgets(self):
        # Navigation Bar to the left
        self.navBar = Frame(self.window, bg="#1b2e38", width=385, height=1024)
        self.navBar.pack(side=LEFT, fill=Y)

        # Logo top left
        logo_label = Label(self.navBar, text="WalletWise", fg="white", bg="#1b2e38", font=("Arial", 24))
        logo_label.pack(pady=(20, 50))

        # Home button
        self.home_button = Button(self.navBar, text="Home", font=("Arial", 20), bg="#1b2e38", fg="white", command=self.show_home)
        self.home_button.pack(fill=X)

        # Budget button
        self.budget_button = Button(self.navBar, text="Budget", font=("Arial", 20), bg="#1b2e38", fg="white", command=self.show_budget)
        self.budget_button.pack(fill=X)
        
        # Main content frame
        self.main_content = Frame(self.window, bg="#FFFFFF", width=997, height=922)
        self.main_content.place(x=385, y=102)

    def clear_frame(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_frame()
        self.current_frame = "Home"
        
        # Search bar
        self.search_bar = Frame(self.main_content, bg="#D9D9D9", width=997, height=102)
        self.search_bar.pack(side=TOP, pady=10)
        search_label = Label(self.search_bar, text="Search", bg="#D9D9D9", font=("Arial", 20))
        search_label.pack(side=LEFT, padx=20)

        # Expense input fields
        Label(self.main_content, text="Expense amount:", font=("Arial", 14)).place(x=50, y=150)
        self.expense_amount_entry = Entry(self.main_content)
        self.expense_amount_entry.place(x=250, y=150, width=200)

        Label(self.main_content, text="Item Description:", font=("Arial", 14)).place(x=50, y=200)
        self.item_description_entry = Entry(self.main_content)
        self.item_description_entry.place(x=250, y=200, width=200)

        Label(self.main_content, text="Date(YYYY-MM-DD):", font=("Arial", 14)).place(x=50, y=250)
        self.date_entry = Entry(self.main_content)
        self.date_entry.place(x=250, y=250, width=200)

        Button(self.main_content, text="Add Expense", command=self.add_expense, font=("Arial", 14)).place(x=250, y=300)
        
        # Transactions listbox
        Label(self.main_content, text="Transactions:", font=("Arial", 14)).place(x=50, y=350)
        self.transactions_listbox = Listbox(self.main_content)
        self.transactions_listbox.place(x=250, y=350, width=400, height=150)
        
        # Edit, Delete, Show Chart, and Exit buttons
        self.edit_expense_button = Button(self.main_content, text="Edit Expense", command=self.edit_expense, font=("Arial", 14))
        self.edit_expense_button.place(x=700, y=350)
        
        self.delete_expense_button = Button(self.main_content, text="Delete Expense", command=self.delete_expense, font=("Arial", 14))
        self.delete_expense_button.place(x=700, y=400)
        
        self.show_chart_button = Button(self.main_content, text="Show Chart", command=self.show_chart, font=("Arial", 14))
        self.show_chart_button.place(x=700, y=450)
        
        self.exit_button = Button(self.main_content, text="Exit", command=self.window.quit, font=("Arial", 14))
        self.exit_button.place(x=700, y=500)

    def show_budget(self):
        self.clear_frame()
        self.current_frame = "Budget"
        
        # Search bar
        self.search_bar = Frame(self.main_content, bg="#D9D9D9", width=997, height=102)
        self.search_bar.pack(side=TOP, pady=10)
        search_label = Label(self.search_bar, text="Search", bg="#D9D9D9", font=("Arial", 20))
        search_label.pack(side=LEFT, padx=20)
        
        # Display budget image (simulated with a placeholder)
        image_path = path.join("/mnt/data", "image.png")
        budget_image = Image.open(image_path)
        budget_image_resized = budget_image.resize((997, 820), Image.LANCZOS)
        self.budget_photo = ImageTk.PhotoImage(budget_image_resized)
        
        self.budget_image_label = Label(self.main_content, image=self.budget_photo, bd=0, highlightthickness=0)
        self.budget_image_label.pack(expand=True)

    def add_expense(self):
        expense = self.expense_amount_entry.get()
        description = self.item_description_entry.get()
        date = self.date_entry.get()
        if expense and description and date:
            self.transactions_listbox.insert(END, f"{date}: {description} - ${expense}")
            self.expense_amount_entry.delete(0, END)
            self.item_description_entry.delete(0, END)
            self.date_entry.delete(0, END)
        else:
            messagebox.showwarning("Input Error", "All fields are required.")
    
    def edit_expense(self):
        try:
            selected_index = self.transactions_listbox.curselection()[0]
            selected_item = self.transactions_listbox.get(selected_index)
            date, rest = selected_item.split(": ")
            description, expense = rest.split(" - $")
            
            self.expense_amount_entry.delete(0, END)
            self.expense_amount_entry.insert(0, expense)
            
            self.item_description_entry.delete(0, END)
            self.item_description_entry.insert(0, description)
            
            self.date_entry.delete(0, END)
            self.date_entry.insert(0, date)
            
            self.transactions_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Select a transaction to edit.")
    
    def delete_expense(self):
        try:
            selected_index = self.transactions_listbox.curselection()[0]
            self.transactions_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Select a transaction to delete.")
    
    def show_chart(self):
        messagebox.showinfo("Show Chart", "Chart functionality not implemented.")
 
        
if __name__ == "__main__":
    app = App()
