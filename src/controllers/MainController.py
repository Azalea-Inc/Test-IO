from IO.SerialInterface import SerialInterface


class MainController:
    observers = []

    def __init__(self):
        self.serialInterface = SerialInterface(self)

    def subscribe(self, observer):
        self.observers.append(observer)

    def isOpenConnection(self):
        self.serialInterface.isOpen()

    def openConnection(self, port):
        self.serialInterface.setPort(port)
        self.serialInterface.open()

    def closeConnection(self):
        self.serialInterface.close()

    def getPorts(self):
        return self.serialInterface.getPorts()

    def sendData(self, data):
        self.serialInterface.sendData(data)

    def update(self, data):
        for observer in self.observers:
            observer.notify(data)
