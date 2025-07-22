from abc import ABC, abstractmethod
class despositivosElectronicos(ABC):
    @abstractmethod
    def encender(self):
        pass
    @abstractmethod
    def apagar(self):
        pass


class Television():
    def encender (self):
        print("television encendida")
    def apagar (self):
        print("television apagada")

class Radio():
    def encender (self):
        print("radio encendida")
    def apagar (self):
        print("radio apagada")


tv=Television()
tv.encender()
tv.apagar()

radio=Radio()
radio.encender()
radio.apagar()
