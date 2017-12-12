

class SetPiece:

    def __init__(self, name, desc, location, formattedname):
        self.name = name
        self.examined = 'false'
        self.cantouch = 'true'
        self.pickup = False
        self.desc = desc
        self.location = location
        self.formattedname = formattedname



mug = SetPiece('mug', "The lone mug. Yes, the lone mug. Apparently they leave it untouched and pristine for whenever the patriarch of the bar comes to drink.", "mug", "the mug")
Stool = SetPiece('stool', 'I feel down from the stool and hurted my head and my life hasn\'t been the same ever since. I been down so long it look like up to me', 'bar', 'a stool')
counter = SetPiece('counter', "It's a counter that is made from the remains of a bunch of doors. This tavern is really cheap and doesn't really spend much on the interior. All the money goes towards mead and ale", "counter", "the counter")
caveDragon = SetPiece('dragon', "It's relaxing. I bet its a good idea to attack it.", "cave", "the dragon")

aleBarrel = SetPiece('barrel', "It's a giant barrel filled with ale. Mother was right. You think. The people here are savages. Just putting a mug into the barrel and drinking another round. Not using the Natural Laws of the world to make the glorious drops of ale fall.", 'tavern', "a barrel")

waterwheel = SetPiece('waterwheel', "You aren't the most educated in the natural sciences. You're not quite sure how this thing works.", "village", "a waterwheel")
wagon = SetPiece('wagon', "This isn't the horse you rode in on. But it's a nice horse nonetheless.", "village", "a wagon")
setPieceList = [Stool, caveDragon, aleBarrel, wagon, waterwheel]
