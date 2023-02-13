import tkinter.font as tkfont
import customtkinter


class LoginPage:
    
    def __init__(self, master):
        frame = customtkinter.CTkFrame(master)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        font = customtkinter.CTkFont(family='Roboto', size=24)
        self.label = customtkinter.CTkLabel(master=frame, text="Login System", font=font)
        self.label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        self.entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")

        self.button = customtkinter.CTkButton(master=frame, text="Login", command="")

        checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")

        self.entry1.pack(pady=10, padx=5)
        self.entry2.pack(pady=10, padx=5)
        self.button.pack(pady=20, padx=10)

        checkbox.pack(pady=10, padx=5)
