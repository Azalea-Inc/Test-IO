import serial
from threading import Thread

import serial.tools.list_ports as serialList


class SerialInterface():
    port = ""
    ports = []

    def __init__(self, mainController):
        self.mainController = mainController

        self.__client = serial.Serial()

    def getPorts(self):
        self.ports = []

        for port, desc, hwid in sorted(serialList.comports()):
            # print("{}: {} [{}]".format(port, desc, hwid))
            self.ports.append(port)

        return self.ports

    def setPort(self, port):
        self.port = port

    def isOpen(self):
        return self.__client.is_open

    def open(self):
        if self.__client.is_open:
            return

        self.__client.port = self.port
        self.start()

    def close(self):
        if not self.__client.is_open:
            return

        self.__client.close()

    def sendData(self, data):
        if (not self.__client.is_open):
            return
        self.__client.write(data.encode())

    def start(self):
        try:
            self.__client.open()
            self.__thread = Thread(target=self.run)
            self.__thread.start()
        except:
            print("Error to connection")

    def run(self):
        while self.__client.is_open:
            try:
                data = self.__client.readline()
                self.mainController.update(data)
            except:
                print("Close Connection")
                self.__client.close()
