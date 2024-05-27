from tkinter import *
from app_settings import *
from os import *
from PIL import ImageTk, Image


class App():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1440x1024")
        self.window.title("WalletWise")

        #Navigation Bar to the left
        self.navBar=Frame(self.window, bg="#1b2e38", width=385, height=1024).pack(side=LEFT)
        
        #@Search Bar up the top
        self.searchBar=Frame(self.window, bg="#D9D9D9", width=997, height=102).pack(side=TOP, pady=25)

        #Logo top left

        image = Image.open("images/WalletWise_logo.png")
        photo = ImageTk.PhotoImage(image.resize((196, 196)))

        self.mainframe=Frame(width=344, height=102)
        self.mainframe.place(x=20,y=22)


        self.home_button = Button(self.window, text="Home", height=5, width=8, command=self.home)
        self.home_button.place(x=20,y=148)

        



        self.window.mainloop()
    
    def home(self):
        self.window.destroy()