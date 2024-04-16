import customtkinter as ctk


class DataSendedView:
    def __init__(self, root):
        self.root = root
        
        self.frame = ctk.CTkFrame(self.root)
        self.frame.grid(row=1, column=1, padx=15, columnspan=2, sticky="new")

        self.frame.grid_rowconfigure(0, weight=1)
