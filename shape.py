class Position: 
    def __init__(self, name:str) -> None:
        self.name = name
        self.token = None

    def assign_token(self, token):
        self.name = token

    def is_occupied(self) -> bool:
        return self.token != None
    


class Token:
    def __init__(self, color) -> None:
        pass


p = Position("A")
print(p.is_occupied())
