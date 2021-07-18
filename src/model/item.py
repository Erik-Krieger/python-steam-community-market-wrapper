

class Item():


    app_id: int
    lowest_price: int
    median_price: int
    volume: int
    name: str


    def __init__(self, app_id: int, lowest_price: int, median_price: int, volume: int, name: str):
        self.app_id = app_id
        self.lowest_price = lowest_price
        self.median_price = median_price
        self.volume = volume
        self.name = name

    def __hash__(self):
        pass

    def __repr__(self):
        pass


    def get_app_id(self):
        return self.app_id

    def get_lowest_price(self):
        return self.lowest_price

    def get_median_price(self):
        return self.median_price

    def get_volume(self):
        return self.volume

    def get_name(self):
        return self.name