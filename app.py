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
        photo = ImageTk.PhotoImage(image.resize((370, 120)))

        #load image 
        self.home=Image.open("images/home.png")
        home=ImageTk.PhotoImage(image.resize((5,5)))



        self.mainframe=Frame(width=344, height=102)
        self.mainframe.place(x=20,y=22)

        self.logo = Label(image=photo)
        self.logo.place(x=6, y=15)

        
        # Load home.png image
        home_image = Image.open("images/home.png")
        self.home_photo = ImageTk.PhotoImage(home_image)

        # Get the size of the image
        width, height = home_image.size

        # Create home button with the same size as the image
        self.home_button = Button(self.window, image=self.home_photo, command=self.home, width=width, height=height)


        # Create home button
        self.home_button = Button(self.window, image=self.home_photo, command=self.home, width=50, height=50)
        self.home_button.image = self.home_photo
        self.home_button.place(x=20, y=148)


        



        self.window.mainloop()
    
    def home(self):
        self.window.destroy()