class SlException(BaseException):
    pass

# int, str, bool, None, float. list

class Symbol():
    name = "Symbol"

    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise SlException("Wrong value " + value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other