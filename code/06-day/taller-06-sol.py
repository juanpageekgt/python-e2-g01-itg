import pickle
import csv

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.product_id} - {self.name}: {self.quantity} units at ${self.price:.2f} each"

class Inventory:
    def __init__(self):
        self.products = {}

    def create_product(self, product_id, name, quantity, price):
        if product_id in self.products:
            print("Product ID already exists!")
        else:
            self.products[product_id] = Product(product_id, name, quantity, price)
            print("Product created successfully.")

    def read_product(self, product_id):
        return self.products.get(product_id, "Product not found.")

    def update_product(self, product_id, name=None, quantity=None, price=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name:
                product.name = name
            if quantity is not None:
                product.quantity = quantity
            if price is not None:
                product.price = price
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def save_to_file(self, filename, filetype="txt"):
        if filetype == "dat":
            with open(filename, "wb") as f:
                pickle.dump(self.products, f)
        elif filetype == "csv":
            with open(filename, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Quantity", "Price"])
                for product in self.products.values():
                    writer.writerow([product.product_id, product.name, product.quantity, product.price])
        else:  # Default to text file
            with open(filename, "w") as f:
                for product in self.products.values():
                    f.write(str(product) + "\n")
        print(f"Data saved to {filename} successfully.")

    def load_from_file(self, filename, filetype="txt"):
        try:
            if filetype == "dat":
                with open(filename, "rb") as f:
                    self.products = pickle.load(f)
            elif filetype == "csv":
                with open(filename, "r") as f:
                    reader = csv.DictReader(f)
                    self.products = {row["ID"]: Product(row["ID"], row["Name"], int(row["Quantity"]), float(row["Price"])) for row in reader}
            else:  # Default to text file
                with open(filename, "r") as f:
                    for line in f:
                        product_id, rest = line.split(" - ")
                        name, details = rest.split(":")
                        quantity, price = details.split(" units at $")
                        self.products[product_id] = Product(product_id, name.strip(), int(quantity), float(price))
            print(f"Data loaded from {filename} successfully.")
        except FileNotFoundError:
            print(f"{filename} not found.")

# Main program
if __name__ == "__main__":
    inventory = Inventory()
    while True:
        print("\nInventory Menu:")
        print("1. Create Product")
        print("2. Read Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.create_product(pid, name, quantity, price)
        elif choice == "2":
            pid = input("Enter product ID: ")
            print(inventory.read_product(pid))
        elif choice == "3":
            pid = input("Enter product ID: ")
            name = input("Enter new name (leave blank to skip): ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            inventory.update_product(pid, name or None, int(quantity) if quantity else None, float(price) if price else None)
        elif choice == "4":
            pid = input("Enter product ID: ")
            inventory.delete_product(pid)
        elif choice == "5":
            filename = input("Enter filename: ")
            filetype = input("Enter filetype (txt/csv/dat): ")
            inventory.save_to_file(filename, filetype)
        elif choice == "6":
            filename = input("Enter filename: ")
            filetype = input("Enter filetype (txt/csv/dat): ")
            inventory.load_from_file(filename, filetype)
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")