from tkinter import *
from app_settings import *
from os import *

class App():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1440x1024")
        self.window.title("WalletWise")

        self.navBar=Frame(self.window, bg="#1b2e38", width=385, height=1024).pack(side=LEFT)
        self.searchBar=Frame(self.window, bg="#D9D9D9", width=997, height=102).pack(side=TOP, pady=25)


        self.logo=Frame()
        self.logo.place(x=20,y=22)


        self.home_button = Button(self.window, text="Home", height=5, width=8, command=self.home)
        self.home_button.place(x=20,y=148)




        self.window.mainloop()
    
    def home(self):
        self.window.destroy()