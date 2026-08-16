"""Q3 - Inventory filtering with regular expressions.

Students: complete this file directly. Do not create another Python file.
"""

import re


PATTERN = (
    r"^Product: (.+) \| Price: ([0-9.]+) \| Stock: ([0-9]+) "
    r"\| SoldLastMonth: ([0-9]+)$"
)

def load_products(file_name):
    """Read valid inventory records and return product data."""
    # TODO:
    # Return a list in which every item contains:
    #    (name, price, stock, sold_last_month)
    with open(file_name) as file:
        item_list = []        
        for line in file:
            data = line.strip()
            reg = re.findall(PATTERN, data)
            if len(reg) == 1:
                name, price, stock, sold = reg[0]
                item = (name, float(price), int(stock), int(sold))
                item_list.append(item)
        return item_list

def find_premium_products(products):
    """Return names of products whose price is at least 50.0."""
    # TODO Part 1
    premium_products = []
    for item in products:
        name, price, stock, sold = item
        if price >= 50.0:
            premium_products.append(name)
    return premium_products
            
def find_reorder_products(products):
    """Return names of products that need to be reordered."""
    # TODO Part 2
    # A product needs to be reordered when stock < 20 and sold_last_month >= 30.
    reorder_product = []
    for item in products:
        name, price, stock, sold = item
        if stock < 15 and sold >= 25:
            reorder_product.append(name)
    return reorder_product

def main():
    products = load_products("inventory.txt")

    premium_products = find_premium_products(products)
    print("Part 1 result:", premium_products)

    reorder_products = find_reorder_products(products)
    print("Part 2 result:", reorder_products)


if __name__ == "__main__":
    main()
