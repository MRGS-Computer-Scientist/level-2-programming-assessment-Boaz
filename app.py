from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from app_settings import *
from os import path
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App():

    def __init__(self):
        super().__init__()

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

        # Search Bar up the top
        self.searchBar = Frame(self.window, bg="#D9D9D9", width=997, height=102)
        self.searchBar.pack(side=TOP, pady=25)

        # Logo top left
        image_path = path.join("images", "WalletWise_logo.png")
        image = Image.open(image_path)
        self.logo_photo = ImageTk.PhotoImage(image.resize((370, 120)))

        self.logo_frame = Frame(self.window, width=344, height=102)
        self.logo_frame.place(x=7, y=22)

        self.logo = Label(self.logo_frame, image=self.logo_photo, bd=0, highlightthickness=0)
        self.logo.pack(expand=True)

        # Load home image
        home_image_path = path.join("images", "home_button.png")
        home_image = Image.open(home_image_path)
        home_image_resized = home_image.resize((200, 75), Image.LANCZOS)
        self.home_photo = ImageTk.PhotoImage(home_image_resized)

        # Create home button
        self.home_button = Button(self.window, image=self.home_photo, command=self.show_home, bd=0, highlightthickness=0, activebackground="#489cac")
        self.home_button.place(x=10, y=150)

        # Load Budget image
        budget_button_path = path.join("images", "budget_button.png")
        budget_image = Image.open(budget_button_path)
        budget_image_resized = budget_image.resize((200, 75), Image.LANCZOS)
        self.budget_photo = ImageTk.PhotoImage(budget_image_resized)

        # Create budget button
        self.budget_button = Button(self.window, image=self.budget_photo, command=self.show_budget, bd=0, highlightthickness=0, activebackground="#489cac")
        self.budget_button.place(x=28, y=235)
        
        # Main content frame
        self.main_content = Frame(self.window, bg="#FFFFFF", width=997, height=922)
        self.main_content.place(x=385, y=102)

    def clear_frame(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_frame()
        self.current_frame = "Home"
        # Add widgets for the home frame here
        Label(self.main_content, text="Home", font=("Arial", 24)).pack(expand=True)

    def show_budget(self):
        self.clear_frame()
        self.current_frame = "Budget"
        # Add widgets for the budget frame here
        Label(self.main_content, text="Budget", font=("Arial", 24)).pack()
        self.create_pie_chart()

    def create_pie_chart(self):
        def add_expense(self):
            pass
        #TO COMPLETE


if __name__ == "__main__":
    app = App()
