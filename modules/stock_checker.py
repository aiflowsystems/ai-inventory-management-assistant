def check_low_stock(inventory_items):
    low_stock_items = []

    for item in inventory_items:
        quantity = int(item["quantity"])
        reorder_level = int(item["reorder_level"])

        if quantity <= reorder_level:
            low_stock_items.append(item)

    return low_stock_items