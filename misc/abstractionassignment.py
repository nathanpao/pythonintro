from abc import abstractmethod, ABC
class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP Scroll")

    @abstractmethod
    def click(self):
        pass

class DELL(TouchScreenLaptop):
    def scroll(self):
        print("Dell Scroll")

    @abstractmethod
    def click(self):
        pass

class HPNotebook(HP):

    def scroll(self):
        super().scroll()

    def click(self):
        print("HP Click")

class DELLNotebook(DELL):

    def scroll(self):
        super().scroll()
    def click(self):
        print("Dell Click")

h = HPNotebook()
h.scroll()
h.click()

d = DELLNotebook()
d.scroll()
d.click()