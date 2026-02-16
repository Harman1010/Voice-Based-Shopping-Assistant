CATEGORY_MAP = {
    "milk": "Dairy",
    "cheese": "Dairy",
    "apple": "Produce",
    "banana": "Produce",
    "bread": "Bakery",
    "chips": "Snacks",
    "chocolate": "Snacks",
    "toothpaste": "Personal Care",
    "soap": "Personal Care",
    "water": "Beverages"
}


def categorize(item):
    for key in CATEGORY_MAP:
        if key in item:
            return CATEGORY_MAP[key]
    return "Other"
