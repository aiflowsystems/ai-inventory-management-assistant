def analyze_inventory(inventory_items):
    total_items = len(inventory_items)
    total_quantity = 0
    total_inventory_value = 0

    for item in inventory_items:
        quantity = int(item["quantity"])
        unit_price = float(item["unit_price"])

        total_quantity += quantity
        total_inventory_value += quantity * unit_price

    return {
        "total_items": total_items,
        "total_quantity": total_quantity,
        "total_inventory_value": round(total_inventory_value, 2)
    }