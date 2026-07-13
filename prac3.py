class Buy:
    def __init__(self):
        # Initialize product attributes
        self.pName = ""
        self.pDes = ""
        self.pCategory = ""
        self.pPrice = 0.0
        self.found = False
    
    def addProduct(self):
        """Add a new product"""
        print("\n--- ADD NEW PRODUCT ---")
        self.pName = input("Enter product name: ")
        self.pDes = input("Enter product description: ")
        self.pCategory = input("Enter product category: ")
        self.pPrice = float(input("Enter product price: Kshs "))
        self.found = False
        print(f"\n✓ Product '{self.pName}' added successfully!")
        print("-" * 40)
    
    def findProduct(self):
        """Find product based on search criteria"""
        print("\n--- FIND PRODUCT ---")
        
        if self.pName == "":
            print("\n✗ No product in the system. Please add a product first.")
            print("-" * 40)
            return
        
        search_category = input("Enter search category: ")
        min_price = float(input("Enter minimum price: Kshs "))
        max_price = float(input("Enter maximum price: Kshs "))
        
        if (self.pCategory == search_category and 
            min_price <= self.pPrice <= max_price):
            self.found = True
            print(f"\n✓ Product found matching your criteria!")
            print(f"  Name: {self.pName}")
            print(f"  Category: {self.pCategory}")
            print(f"  Price: Kshs {self.pPrice:,.2f}")
        else:
            self.found = False
            print("\n✗ No product found matching your search criteria.")
        print("-" * 40)
    
    def myCart(self):
        """Display the product in cart"""
        print("\n--- MY CART ---")
        
        if self.found and self.pName != "":
            print("=" * 80)
            print(f"{'Product Name':<20} {'Description':<25} {'Category':<15} {'Price':<15}")
            print("=" * 80)
            print(f"{self.pName:<20} {self.pDes:<25} {self.pCategory:<15} Kshs {self.pPrice:,.2f}")
            print("=" * 80)
            print(f"Total: Kshs {self.pPrice:,.2f}")
        else:
            print("\nYour cart is empty.")
            print("Please add a product and find it first before viewing the cart.")
        print("-" * 40)
    
    def exitProgram(self):
        """Exit the program"""
        print("\nThank you for using Deals Poa Catalogue!")
        print("Exiting program...")
        return False

def main():
    """Main program loop"""
    b = Buy()
    running = True
    
    while running:
        print("*" * 50)
        print("\t\tDeals Poa Catalogue")
        print("*" * 50)
        print("\t\t1. Add New Product")
        print("\t\t2. Find Product")
        print("\t\t3. My Cart")
        print("\t\t4. Exit")
        print("*" * 50)
        
        userChoice = input("\nEnter your choice (1-4): ")
        
        # Simple validation using basic conditions
        if userChoice == "1":
            b.addProduct()
        elif userChoice == "2":
            b.findProduct()
        elif userChoice == "3":
            b.myCart()
        elif userChoice == "4":
            running = b.exitProgram()
        else:
            print("\n✗ Invalid choice! Please enter 1, 2, 3, or 4.")
        
        if running:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()