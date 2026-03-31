# Emergency Operations Center (EOC) Resource System

A lightweight, Python-based terminal application designed to track critical supplies during disaster relief operations. This system ensures that emergency responders can monitor inventory levels, log new shipments, and track deployments with data persistence.

## 🚀 Features

* **Real-time Inventory Tracking:** View current stock levels, units of measurement, and priority status in a formatted table.
* **Smart Supply/Deployment Logging:**
    * Add stock using positive integers (e.g., `+50`).
    * Deploy stock using negative integers (e.g., `-20`).
    * **Validation:** Prevents "negative inventory" to avoid over-deployment errors.
* **Data Persistence:** Automatically saves all changes to a `disaster_data.csv` file for long-term availability.
* **Emergency Defaults:** If no database file is found on the first run, the system auto-populates with critical resources like Drinking Water, Rations, and Power Generators.

## 🛠️ Installation & Setup

1.  **Requirement:** Ensure you have [Python 3.x](https://www.python.org/) installed.
2.  **Download:** Save the script (e.g., `main.py`) to your local machine.
3.  **Run:** Open your terminal or command prompt and execute:
    ```bash
    python main.py
    ```

## 📋 How to Use

When the program starts, you will be presented with the main menu:

1.  **View Current Inventory:** Displays a formatted table of all resources currently in the system.
2.  **Log New Supply/Deployment:**
    * Enter the resource name (e.g., `Blankets`).
    * If the item exists, enter the change in quantity.
    * If the item is new, the system will prompt you for the unit (e.g., Kg, Units, Liters) and priority level (e.g., Critical, High, Med, Low).
3.  **Exit System:** Saves all data securely to the CSV and shuts down the application.

## 💾 Data Structure

The system stores data in a CSV format, making it easy to open in Excel or Google Sheets for external reporting or auditing.

| Field | Description |
| :--- | :--- |
| **item** | The name of the resource (e.g., First Aid Kits) |
| **qty** | The current numerical count |
| **unit** | The measurement unit (e.g., Liters, Pieces) |
| **priority** | The urgency level (Critical, High, Medium, Low) |

---

## ✍️ Author & Course Information

* **Author: Akshaath A** 
* **Course: python essentials**
* **Branch: B Tech. Bioengineering** 
* **Reg No.: 25BOE10027** 

---
