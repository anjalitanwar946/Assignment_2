dominos = ["margherita", "paneer pizza", "garlic bread", "zingi parcel", "chicken wings"]
price = {
    "margherita": 110, "paneer pizza": 180, "garlic bread": 109, "zingi parcel": 69, "chicken wings": 189
}
orders = []


def place_order(Name, Address, Pizzas):
   
    order = {
        "Name": Name,
        "Address": Address,
        "pizzas": Pizzas,
    }
    orders.append(order)
    print("Order placed successfully")


place_order("anjali", "nai sadak", {"margherita": 2, "paneer pizza": 1})
place_order("kunnu", "gadha puliya", {"chicken wings": 3, "zingi parcel": 1})


def display_orders():
    print("All Orders:")
    for index, order in enumerate(orders, start=1):
        print(f"Order {index}:")
        print(f"Customer Name: {order['Name']}")
        print(f"Customer Address: {order['Address']}")
        print("Pizzas:")
        for pizza, quantity in order['pizzas'].items():
            print(f" {pizza}: {quantity}")
        print()

display_orders()