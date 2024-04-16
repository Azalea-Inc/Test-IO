import customtkinter as ctk


class ControlsView:
    def __init__(self, root, paramsView, mainController):
        self.root = root
        self.paramsView = paramsView

        self.mainController = mainController

        self.setup()

    def setup(self):
        self.openButton = ctk.CTkButton(
            self.root, text="Open", width=100, command=self.openConnection)
        self.openButton.grid(
            row=3, column=1, padx=(5, 15), pady=30, sticky="we")

        self.closeButton = ctk.CTkButton(
            self.root, text="Close", width=100, fg_color="transparent", border_width=2, command=self.closeConnection)
        self.closeButton.grid(
            row=3, column=0, padx=(15, 5), pady=30, sticky="w")

    def openConnection(self):
        port = self.paramsView.getPort()
        if (port == None):
            return

        self.mainController.openConnection(port)

    def closeConnection(self):
        self.mainController.closeConnection()
