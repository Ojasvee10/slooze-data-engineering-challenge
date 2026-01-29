from bs4 import BeautifulSoup

def parse_products(html, category):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    # Updated selector (more generic)
    cards = soup.find_all("div", class_=lambda x: x and "prd" in x)

    for card in cards[:30]:  # limit for safety
        product = {
            "product_name": None,
            "category": category,
            "price": None,
            "supplier_name": None,
            "supplier_location": None,
            "min_order_qty": None,
            "rating": None
        }

        h3 = card.find("h3")
        if h3:
            product["product_name"] = h3.get_text(strip=True)

        price = card.find("span", class_=lambda x: x and "price" in x.lower())
        if price:
            product["price"] = price.get_text(strip=True)

        supplier = card.find("a", class_=lambda x: x and "supplier" in x.lower())
        if supplier:
            product["supplier_name"] = supplier.get_text(strip=True)

        city = card.find("span", class_=lambda x: x and "city" in x.lower())
        if city:
            product["supplier_location"] = city.get_text(strip=True)

        products.append(product)

    return products