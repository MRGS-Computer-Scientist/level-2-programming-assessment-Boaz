from tkinter import *

window = Tk()
window.geometry("1440x1024")
window.title("WalletWise")

navBar=Frame(window, bg="#1b2e38", width=385, height=1024).pack(side=LEFT)

searchBar=Frame(window, bg="#D9D9D9", width=997, height=102).pack(side=TOP, pady=25)



window.mainloop()
