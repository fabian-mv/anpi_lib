import enum


class ErrorType(enum.Enum):
    ABSOLUTO = "Error absoluto"
    RELATIVO = "Error relativo"
    FUNCION = "Error de la función"


class Result:

    def __init__(self, description="", value=None, iteration: int = None, err: float = None, err_type: ErrorType = None,
                 arg=None, iter_max: int = None):
        self.description = description
        self.value = value
        self.iteration = iteration
        self.err = err
        self.err_type = err_type
        self.arg = arg
        self.iter_max = iter_max

    def print_all(self):
        if self.value:
            payload = vars(self)
            print([f"{k}: {v}" for k, v in payload.items() if payload[k]])
            return self
        else:
            print("ERROR")
            return self
