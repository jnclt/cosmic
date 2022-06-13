from model import Batch, OrderLine


def test_allocate_reduces_stock():
    batch = Batch("batch-001", "sku-table", 10)
    order_line = OrderLine("order-ref", "sku-table", 2)

    batch.allocate(order_line)

    assert batch.quantity == 8
