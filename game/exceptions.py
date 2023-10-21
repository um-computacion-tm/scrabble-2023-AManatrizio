class InvalidWordException(Exception):
    def __init__(self, message="Palabra no válida"):
        self.message = message
        super().__init__(self.message)

class InvalidPlaceWordException(Exception):
    def __init__(self, message="Ubicación de palabra no válida"):
        self.message = message
        super().__init__(self.message)