def get_item_name(existing_items):
    """
    Prompt the user for an item name and ensure it's not a duplicate.
    :param existing_items: A set of existing item names to avoid duplicates.
    :return: The validated item name or None if the user types 'done'.
    """
    while True:
        item_name = input('Enter item name (or done to finish): ').strip()
        if not item_name:
            print("Item name cannot be empty. Please try again.")
            continue
        if item_name.lower() == 'done':
            return None
        if item_name in existing_items:
            print('Item already in cart. Select another item.')
            continue
        return item_name

def get_item_price():
    """
    Prompt the user for the item price and ensure it's a valid positive number.
    :return: The validated price as a float.
    """
    while True:
        try:
            price = float(input('Enter item price: ').strip())
            if price <= 0:
                print('Price cannot be negative or zero. Please enter a valid price.')
                continue
            return price
        except ValueError:
            print('Invalid Price. Please enter a numeric value.')

def get_discounts():
    """
    Prompt the user for discounts as percentages and validate them.
    :return: A list of valid discounts as floats.
    """
    discounts = input('Enter discounts (if any, separated by spaces): ').strip().split()
    valid_discounts = []
    for discount in discounts:
        try:
            discount_value = float(discount)
            if 0 <= discount_value <= 100:
                valid_discounts.append(discount_value)
            else:
                print(f'Invalid discount figure: {discount}. Discount must be between 0 and 100.')
        except ValueError:
            print(f'Invalid discount: {discount}. Please enter a numeric value.')
    return valid_discounts

def get_item_details():
    """
    Prompt the user for additional item details (key-value pairs).
    :return: A dictionary of item details.
    """
    details_input = input('Enter item details (e.g., Colour->Red Size->Large): ').strip()
    details = {}
    if details_input:
        for detail in details_input.split():
            try:
                key, value = detail.split("->")
                details[key] = value
            except ValueError:
                print(f'Invalid detail format: {detail}. Skipping. Use Key->Value format.')
    return details

def add_to_cart(cart, item_names):
    """
    Combine all functionalities to add an item to the cart.
    :param cart: List to store cart items.
    :param item_names: Set to track item names and avoid duplicates.
    """
    # Step 1: Get the item name
    item_name = get_item_name(item_names)
    if item_name is None:  # User typed 'done'
        return False

    # Step 2: Get the item price
    item_price = get_item_price()

    # Step 3: Get any discounts
    discounts = get_discounts()

    # Step 4: Get additional item details
    details = get_item_details()

    # Step 5: Apply discounts to calculate the final price
    final_price = item_price
    for discount in discounts:
        final_price -= final_price * (discount / 100)

    # Step 6: Add the item to the cart
    cart.append({
        "name": item_name,
        "final_price": round(final_price, 2),
        "details": details
    })
    item_names.add(item_name)

    print(f"Item added: {item_name} - Final Price: ${round(final_price, 2)}\n")
    return True

def display_cart_summary(cart):
    """
    Display the cart summary including item details and total cost.
    :param cart: List of items in the cart.
    """
    print("\n--- Cart Summary ---")
    if not cart:
        print("Your cart is empty!")
        return

    total_cost = 0
    for item in cart:
        details = ", ".join(f"{key}={value}" for key, value in item["details"].items())
        print(f"{item['name']} - ${item['final_price']} ({details})")
        total_cost += item['final_price']

    print(f"Total Cost: ${round(total_cost, 2)}")

def main():
    """
    Main shopping cart program loop.
    """
    cart = []          # List to store cart items
    item_names = set()  # Set to track unique item names

    print("Welcome to the Shopping Cart Program!")
    while True:
        # Call the add_to_cart function
        if not add_to_cart(cart, item_names):
            break  # Exit loop if user types 'done'

    # Display the cart summary
    display_cart_summary(cart)

if __name__ == "__main__":
    main()
