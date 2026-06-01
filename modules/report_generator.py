def generate_inventory_report(inventory_summary, low_stock_items):
    low_stock_text = ""

    for item in low_stock_items:
        low_stock_text += (
            f"{item['item_name']} | "
            f"Quantity: {item['quantity']} | "
            f"Reorder Level: {item['reorder_level']}\n"
        )

    report = f"""AI Inventory Management Assistant Report

Inventory Summary
=================

Total Items: {inventory_summary['total_items']}
Total Quantity: {inventory_summary['total_quantity']}
Total Inventory Value: ${inventory_summary['total_inventory_value']}

Low Stock Items
===============

{low_stock_text}
"""

    return report