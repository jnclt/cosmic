def test_allocate_reduces_stock():
    batch = Batch("ref1", "sku-table", 10)
    order_line = OrderLine("sku_table", 2)

    batch.allocate(order_line)

    assert batch.quantity == 8
