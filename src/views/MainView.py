import customtkinter as ctk
from views.Main.AsideView import AsideView
from views.Main.DataView import DataView

from controllers.MainController import MainController

ctk.set_appearance_mode("System")


class MainView(ctk.CTk):
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        self.mainController = MainController()

        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Test IO")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.setup()

    def setup(self):
        AsideView(self, self.mainController)
        DataView(self, self.mainController)

    def close(self):
        self.mainController.closeConnection()
        self.destroy()
