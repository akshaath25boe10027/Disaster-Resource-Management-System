import csv
import os

class DisasterResourceSystem:
    def __init__(self, db_file="disaster_data.csv"):
        self.db_file = db_file
        self.inventory = {}
        self.load_from_disk()

    def load_from_disk(self):
        """
        Loads data from disk. If no file is found, populates the system
        with critical default emergency resources.
        """
        if os.path.exists(self.db_file):
            with open(self.db_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.inventory[row['item']] = {
                        "qty": int(row['qty']),
                        "unit": row['unit'],
                        "priority": row['priority']
                    }
            print(f"--- System Restored: {len(self.inventory)} resources loaded ---")
        else:
            print("--- No existing data found. Loading Emergency Defaults... ---")
            # DEFAULT EMERGENCY RESOURCES
            self.inventory = {
                "Drinking Water": {"qty": 5000, "unit": "Liters", "priority": "Critical"},
                "Emergency Rations": {"qty": 1200, "unit": "Packs", "priority": "High"},
                "First Aid Kits": {"qty": 150, "unit": "Units", "priority": "High"},
                "Blankets": {"qty": 300, "unit": "Pieces", "priority": "Medium"},
                "Flashlights": {"qty": 100, "unit": "Units", "priority": "Medium"},
                "Power Generators": {"qty": 5, "unit": "Units", "priority": "Critical"}
            }
            self.save_to_disk() # Save defaults to a new CSV immediately

    def save_to_disk(self):
        """Writes memory state to CSV for long-term availability."""
        with open(self.db_file, mode='w', newline='') as file:
            fieldnames = ['item', 'qty', 'unit', 'priority']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item, details in self.inventory.items():
                writer.writerow({
                    'item': item,
                    'qty': details['qty'],
                    'unit': details['unit'],
                    'priority': details['priority']
                })

    def update_resource(self):
        print("\n[Input Resource Data]")
        name = input("Resource Name: ").strip().title()
        try:
            qty_change = int(input("Quantity change (+ to add, - to remove): "))
            
            if name in self.inventory:
                new_total = self.inventory[name]['qty'] + qty_change
                if new_total < 0:
                    print("!!! Error: Insufficient stock for deployment !!!")
                else:
                    self.inventory[name]['qty'] = new_total
                    print(f"Updated {name}. New Balance: {new_total}")
            else:
                unit = input("Unit (e.g., Kg, Liters): ")
                priority = input("Priority (Critical/High/Med/Low): ")
                self.inventory[name] = {"qty": max(0, qty_change), "unit": unit, "priority": priority}
                print(f"New Resource '{name}' registered.")

            self.save_to_disk()
            print(">> Transaction Logged.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def view_status(self):
        print("\n" + "="*50)
        print(f"{'RESOURCE':<18} | {'QTY':<6} | {'UNIT':<10} | {'PRIORITY'}")
        print("-" * 50)
        for item, d in self.inventory.items():
            print(f"{item:<18} | {d['qty']:<6} | {d['unit']:<10} | {d['priority']}")
        print("="*50)

def main():
    system = DisasterResourceSystem()
    while True:
        print("\nEMERGENCY OPERATIONS CENTER")
        print("1. View Current Inventory")
        print("2. Log New Supply/Deployment")
        print("3. Exit System")
        
        choice = input("\nSelect Option (1-3): ")
        
        if choice == '1':
            system.view_status()
        elif choice == '2':
            system.update_resource()
        elif choice == '3':
            print("Data secured in disaster_data.csv. Shutting down.")
            break

if __name__ == "__main__":
    main()
