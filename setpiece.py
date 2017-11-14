class SetPiece:

    def __init__(self, id, name, desc, location):
        self.id = id
        self.name = name
        self.examined = 'false'
        self.cantouch = 'true'
        self.pickup = False
        self.desc = desc
        self.location = location
