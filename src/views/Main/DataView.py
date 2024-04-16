import customtkinter as ctk
from CTkListbox import *


class DataView:
    def __init__(self, root, mainController):
        self.root = root
        self.mainController = mainController
        self.mainController.subscribe(self)

        self.frame = ctk.CTkFrame(self.root)
        self.frame.grid(row=0, column=1, padx=15, pady=(10, 15), sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=0)

        self.setup()

    def setup(self):

        self.dataInput = ctk.CTkEntry(self.frame)
        self.dataInput.grid(row=0, column=0, padx=15, pady=15,
                            columnspan=1, sticky="new")

        self.sendButton = ctk.CTkButton(
            self.frame, text="Send", width=50, command=self.send)
        self.sendButton.grid(row=0, column=1, padx=(
            0, 15), pady=15, sticky="nwe")

        self.listbox = CTkListbox(self.frame)
        self.listbox.grid(row=1, column=0, padx=15, pady=15,
                          columnspan=2, sticky="nwe")

    def send(self):
        self.mainController.sendData("Data")

    def notify(self, data):
        self.listbox.insert("END", f"{data}")
