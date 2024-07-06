class ShoppingCart:

    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, item:str):
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> list[str]:
        pass

    def get_total_price(self, pricemap) -> int:
        pass