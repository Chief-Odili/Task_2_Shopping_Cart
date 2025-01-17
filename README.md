
# Shopping Cart Program

This program simulates a shopping cart system where users can add items, enter their prices, apply discounts, and provide additional item details (like color or size). The cart keeps track of item names to avoid duplicates and calculates the total cost of all items added.


## Features
- Add items to the cart: Users can input item names, prices, and additional details.
- Avoid duplicate item names: Ensures that no two items with the same name can be added to the cart.
- Apply discounts: Users can apply multiple discounts (in percentages) to each item.
- Calculate the final price: The program computes the price after applying discounts and displays the final price.
- Display cart summary: At the end, users can view a summary of all items added to the cart along with their details and the total cost.



## Function
- get_item_name(existing_items)
Prompts the user for an item name and ensures it's not a duplicate.

Input: A set of existing item names to check for duplicates.
Output: The validated item name or None if the user types 'done' to finish.
- get_item_price()
Prompts the user for the price of an item and ensures it's a valid positive number.

Input: The item price as a float.
Output: The validated item price.
- get_discounts()
Prompts the user for discounts (as percentages) and ensures they are valid numbers between 0 and 100.

Input: A string of space-separated discount values.
Output: A list of valid discounts as floats.
- get_item_details()
Prompts the user for additional item details in a key-value format (e.g., "Color->Red Size->Large").

Input: A string of space-separated key-value pairs.
Output: A dictionary containing the parsed item details.
- add_to_cart(cart, item_names)
Combines all functionalities to add an item to the cart, including obtaining the name, price, discounts, and details.

Input:
cart: A list to store cart items.
item_names: A set to track unique item names.
Output:
True if an item is successfully added.
False if the user types 'done' to exit.
- display_cart_summary(cart)
Displays a summary of all items in the cart, including item names, final prices after discounts, and the total cost.

Input: cart: A list of items in the cart.
Output: Prints a summary to the console.
- main()
The main program loop that orchestrates the user interaction. It calls the add_to_cart function repeatedly until the user decides to finish (by typing 'done'), then displays the cart summary.

Input: None (user interaction is through input prompts).
Output: Displays the cart summary to the console.
