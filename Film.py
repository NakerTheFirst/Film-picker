import Item


class Film(Item):
    def __init__(self, item_id, name, file, energy):
        super().__init__(item_id, name, file)
        self._energy = energy
