# AI Inventory Management Assistant

An AI-powered inventory management assistant that analyzes stock levels, detects low inventory items, calculates inventory value, and generates structured inventory reports.

Designed to help businesses track inventory, identify restocking needs, and automate inventory reporting workflows.

---

## Features

### Inventory Management

- Read inventory data from CSV files
- Track stock quantities
- Track unit prices
- Monitor reorder levels

### Inventory Analysis

- Calculate total inventory items
- Calculate total inventory quantity
- Calculate total inventory value
- Generate inventory statistics

### Low Stock Detection

- Identify items below reorder thresholds
- Highlight restocking needs
- Support inventory monitoring workflows

### Inventory Reporting

- Generate centralized inventory reports
- Summarize inventory metrics
- List low-stock items
- Save reports automatically in the outputs folder

---

## Technologies Used

- Python
- CSV Processing
- JSON Configuration
- File Handling
- Pathlib
- Modular Programming
- Inventory Automation
- Business Process Automation

---

## Project Structure

```text
ai-inventory-management-assistant/

├── main.py
├── config.json
├── inventory.csv
├── README.md
├── .gitignore
│
├── modules/
│   ├── inventory_analyzer.py
│   ├── stock_checker.py
│   └── report_generator.py
│
└── outputs/
    └── inventory_report.txt
```

---

## Workflow

1. Load configuration from `config.json`
2. Read inventory records from `inventory.csv`
3. Analyze inventory quantities and value
4. Detect low-stock items
5. Generate a centralized inventory report
6. Save the report inside the outputs folder

---

## Example Inventory Input

```csv
item_id,item_name,quantity,unit_price,reorder_level
1,Laptop,12,850,5
2,Keyboard,4,40,10
3,Monitor,7,220,6
4,Mouse,3,25,8
5,USB Cable,25,8,15
```

---

## Example Console Output

```text
AI Inventory Management Assistant
=================================

Inventory items loaded: 5
Laptop - 12
Keyboard - 4
Monitor - 7
Mouse - 3
USB Cable - 25

INVENTORY SUMMARY
-----------------
Total Items: 5
Total Quantity: 51
Total Inventory Value: $12175.0

LOW STOCK ITEMS
---------------
Keyboard - Quantity: 4 - Reorder Level: 10
Mouse - Quantity: 3 - Reorder Level: 8

Inventory report generated: outputs\inventory_report.txt
```

---

## Business Value

Inventory management often requires manually reviewing stock levels, calculating inventory value, and identifying products that need replenishment.

This project demonstrates how automation can simplify inventory monitoring by generating inventory metrics and restocking alerts automatically.

---

## Future Improvements

- AI-generated inventory insights
- Inventory forecasting
- Supplier management
- Reorder recommendations
- Multi-warehouse support
- Dashboard interface
- Email alerts
- Barcode integration
- Scheduled inventory reporting

---

## Author

Adam Zaki

AI Automation Developer

GitHub:
https://github.com/aiflowsystems

Portfolio:
https://aiflowsystems.github.io/portfolio/