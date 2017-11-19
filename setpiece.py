class SetPiece:

    def __init__(self, id, name, desc, location):
        self.id = id
        self.name = name
        self.examined = 'false'
        self.cantouch = 'true'
        self.pickup = False
        self.desc = desc
        self.location = location

theDragon = SetPiece(550, 'dragon', 'better run. better pray', 'village')
barSetPiece = SetPiece(445, 'bar', 'call your friends and get drunk', 'village')
setPieceList = [theDragon, barSetPiece]
