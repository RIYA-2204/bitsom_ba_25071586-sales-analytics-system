def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries
    """
    transactions = []

    for line in raw_lines:
        try:
            parts = line.split("|")

            # Must have exactly 8 fields
            if len(parts) != 8:
                continue

            transaction = {
                "TransactionID": parts[0],
                "Date": parts[1],
                "ProductID": parts[2],
                "ProductName": parts[3].replace(",", ""),  # remove commas
                "Quantity": int(parts[4]),
                "UnitPrice": float(parts[5].replace(",", "")),
                "CustomerID": parts[6],
                "Region": parts[7]
            }

            transactions.append(transaction)

        except Exception:
            # skip bad rows
            continue

    return transactions

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    valid_transactions = []
    invalid_count = 0

    filter_summary = {
        "total_input": len(transactions),
        "invalid": 0,
        "filtered_by_region": 0,
        "filtered_by_amount": 0,
        "final_count": 0
    }

    for tx in transactions:
        try:
            # basic validation rules
            if (
                not tx["TransactionID"].startswith("T")
                or not tx["ProductID"].startswith("P")
                or not tx["CustomerID"].startswith("C")
                or tx["Quantity"] <= 0
                or tx["UnitPrice"] <= 0
            ):
                invalid_count += 1
                continue

            amount = tx["Quantity"] * tx["UnitPrice"]

            # region filter
            if region and tx["Region"] != region:
                filter_summary["filtered_by_region"] += 1
                continue

            # amount filters
            if min_amount and amount < min_amount:
                filter_summary["filtered_by_amount"] += 1
                continue

            if max_amount and amount > max_amount:
                filter_summary["filtered_by_amount"] += 1
                continue

            valid_transactions.append(tx)

        except Exception:
            invalid_count += 1

    filter_summary["invalid"] = invalid_count
    filter_summary["final_count"] = len(valid_transactions)

    return valid_transactions, invalid_count, filter_summary

def calculate_total_revenue(transactions):
    total = 0
    for tx in transactions:
        total += tx["Quantity"] * tx["UnitPrice"]
    return total

def revenue_by_region(transactions):
    region_revenue = {}

    for tx in transactions:
        region = tx["Region"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if region not in region_revenue:
            region_revenue[region] = 0

        region_revenue[region] += amount

    return region_revenue

def top_selling_products(transactions, top_n=5):
    product_sales = {}

    for tx in transactions:
        product = tx["ProductName"]
        quantity = tx["Quantity"]

        if product not in product_sales:
            product_sales[product] = 0

        product_sales[product] += quantity

    # sort products by quantity sold (descending)
    sorted_products = sorted(
        product_sales.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_products[:top_n]

def top_customers(transactions, top_n=5):
    customer_spend = {}

    for tx in transactions:
        customer = tx["CustomerID"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if customer not in customer_spend:
            customer_spend[customer] = 0

        customer_spend[customer] += amount

    # sort customers by total spend (descending)
    sorted_customers = sorted(
        customer_spend.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_customers[:top_n]

def daily_sales_trend(transactions):
    daily_sales = {}

    for tx in transactions:
        date = tx["Date"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if date not in daily_sales:
            daily_sales[date] = 0

        daily_sales[date] += amount

    # sort by date
    sorted_daily_sales = dict(sorted(daily_sales.items()))
    return sorted_daily_sales

def daily_sales_trend(transactions):
    daily_sales = {}

    for tx in transactions:
        date = tx["Date"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if date not in daily_sales:
            daily_sales[date] = 0

        daily_sales[date] += amount

    return daily_sales
