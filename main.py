import tkinter.font as tkfont
import customtkinter
from login import LoginPage

customtkinter.set_appearance_mode("Dark")
customtkinter.set_appearance_mode("dark-blue")

root = customtkinter.CTk()
root.geometry("800x500")


app = LoginPage(root)
root.mainloop()