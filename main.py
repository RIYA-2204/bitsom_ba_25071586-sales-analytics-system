from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_transactions,
    validate_and_filter,
    calculate_total_revenue,
    revenue_by_region,
    top_selling_products,
    top_customers,
    daily_sales_trend
)
from utils.report_generator import generate_report


def main():
    print("Starting Sales Analytics System...\n")

    lines = read_sales_data("data/sales_data.txt")
    transactions = parse_transactions(lines)

    valid_tx, _, _ = validate_and_filter(transactions)

    total_revenue = calculate_total_revenue(valid_tx)
    region_sales = revenue_by_region(valid_tx)
    top_products = top_selling_products(valid_tx)
    customers = top_customers(valid_tx)
    daily_sales = daily_sales_trend(valid_tx)

    generate_report(
        total_revenue,
        region_sales,
        top_products,
        customers,
        daily_sales
    )

    print("Report generated successfully!")
    print("Check output/sales_report.txt")


if __name__ == "__main__":
    main()
