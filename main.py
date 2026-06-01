import csv
import json
from pathlib import Path
from modules.inventory_analyzer import analyze_inventory
from modules.stock_checker import check_low_stock
from modules.report_generator import generate_inventory_report

with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

output_folder = config["output_folder"]
Path(output_folder).mkdir(exist_ok=True)

inventory_items = []

with open("inventory.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        inventory_items.append(row)

inventory_summary = analyze_inventory(inventory_items)
low_stock_items = check_low_stock(inventory_items)
inventory_report = generate_inventory_report(
    inventory_summary,
    low_stock_items
)

print("AI Inventory Management Assistant")
print("=================================")
print()

print(f"Inventory items loaded: {len(inventory_items)}")

for item in inventory_items:
    print(item["item_name"], "-", item["quantity"])

print()
print("INVENTORY SUMMARY")
print("-----------------")
print(f"Total Items: {inventory_summary['total_items']}")
print(f"Total Quantity: {inventory_summary['total_quantity']}")
print(f"Total Inventory Value: ${inventory_summary['total_inventory_value']}")

print()
print("LOW STOCK ITEMS")
print("---------------")

for item in low_stock_items:
    print(
        f"{item['item_name']} - "
        f"Quantity: {item['quantity']} - "
        f"Reorder Level: {item['reorder_level']}"
    )

report_file = (
    Path(output_folder)
    / config["inventory_report_file"]
)

with open(report_file, "w", encoding="utf-8") as file:
    file.write(inventory_report)

print()
print(f"Inventory report generated: {report_file}")
