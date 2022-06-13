from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    order_id: str
    sku: str
    quantity: int


class Batch:
    def __init__(self, ref: str, sku: str, quantity: int):
        self.ref = ref
        self.sku = sku
        self.quantity = quantity

    def allocate(self, line: OrderLine):
        self.quantity -= line.quantity
