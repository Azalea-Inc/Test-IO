import customtkinter as ctk
from views.Main.ParamsView import ParamsView
from views.Main.ControlsView import ControlsView


class AsideView:
    def __init__(self, root, mainController):
        self.root = root
        self.mainController = mainController

        self.sidebar = ctk.CTkFrame(self.root, width=100, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.sidebar.grid_columnconfigure((0,  1), weight=1)

        self.setup()

    def setup(self):
        self.paramsView = ParamsView(self.sidebar, self.mainController)
        ControlsView(self.sidebar, self.paramsView, self.mainController)

        # CONNECTION
        self.connectionLabel = ctk.CTkLabel(
            self.sidebar, text="Connection", font=ctk.CTkFont(size=20), anchor="w")
        self.connectionLabel.grid(
            row=0, column=0, padx=(15, 5), pady=15)

        self.refreshButton = ctk.CTkButton(
            self.sidebar, text="Refresh", width=50, command=self.refresh)
        self.refreshButton.grid(
            row=0, column=1, padx=(5, 15), pady=10, sticky="e")

    def refresh(self):
        self.paramsView.setPorts()
