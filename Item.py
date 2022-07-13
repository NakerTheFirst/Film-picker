class Item:
    _item_id = None
    _name = None
    _file = None

    def __init__(self, item_id, name, file):
        self._item_id = item_id
        self._name = name
        self._file = file

    def _get_items_by_line(self, file):
        """Print contents of a file line by line"""

        content = []
        empty = []
        self._item_id = 1

        with open(self.file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                content.append(f"{self.item_id}. {line}")
                self.item_id += 1

            if content == empty:
                return "\nThe file is empty"
            if content != empty:
                return "\n".join(content)

    def _pick_rand_item(item, file):
        """Pick a random item from a list"""
        pass

    def _add_item(item, file):
        with open("films.txt", "a") as f:
            pass

    def _del_item(item, file):
        """Delete an item from file contents"""
        pass

    def _check_if_exists(self, file):
        if exists(file):
            return True

        if not exists(file):
            print("Nothing to show")
            return False
