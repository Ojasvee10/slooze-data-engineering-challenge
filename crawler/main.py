import csv
from fetcher import fetch_page
from parser import parse_products
from utils import polite_delay, current_timestamp

URLS = {
    "Industrial Machinery": "https://dir.indiamart.com/impcat/industrial-machinery.html"
}

output_file = "data/raw/indiamart_industrial_machinery.csv"

all_data = []

for category, url in URLS.items():
    print(f"Scraping category: {category}")
    html = fetch_page(url)
    products = parse_products(html, category)

    for item in products:
        item["scraped_at"] = current_timestamp()
        item["source_url"] = url
        all_data.append(item)

    polite_delay()

# ✅ ALWAYS write headers even if no data
fieldnames = [
    "product_name",
    "category",
    "price",
    "supplier_name",
    "supplier_location",
    "min_order_qty",
    "rating",
    "scraped_at",
    "source_url"
]

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    if all_data:
        writer.writerows(all_data)

print(f"Scraping finished. Records collected: {len(all_data)}")