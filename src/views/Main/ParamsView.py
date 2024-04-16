import customtkinter as ctk


class ParamsView:
    baudrates = ["9600"]
    ports = []
    port = None

    def __init__(self, root, mainController):
        self.root = root
        self.mainController = mainController

        self.setup()
        self.initialize()

    def initialize(self):
        self.setPorts()

    def setup(self):
        self.portLabel = ctk.CTkLabel(
            self.root, text="Port", font=ctk.CTkFont(size=15), width=100, anchor="w")
        self.portLabel.grid(row=1, column=0, padx=(15, 5),
                            pady=(20, 10), sticky="w")

        self.portMenu = ctk.CTkOptionMenu(
            self.root, variable=self.port, values=[*self.ports], width=100)
        self.portMenu.grid(row=1, column=1, padx=(
            5, 15), pady=(20, 10), sticky="w")

        self.portMenu.set("Select Port")

        # BAUDRATE
        self.baudrateLabel = ctk.CTkLabel(
            self.root, text="BaudRate", font=ctk.CTkFont(size=15), width=100, anchor="w")
        self.baudrateLabel.grid(row=2, column=0, padx=(15, 5),
                                pady=10, sticky="we")

        self.baudrateMenu = ctk.CTkOptionMenu(
            self.root, values=self.baudrates, width=100)
        self.baudrateMenu.grid(row=2, column=1, padx=(
            5, 15), pady=10, sticky="we")

    def setPorts(self):
        self.portMenu.configure(values=[])
        self.ports = self.mainController.getPorts()

        if self.ports == []:
            self.port = None
            self.portMenu.set("Select Port")
            return

        self.port = self.ports[0]
        self.portMenu.set(self.ports[0])
        self.portMenu.configure(values=self.ports)

    def getPort(self):
        return self.port
