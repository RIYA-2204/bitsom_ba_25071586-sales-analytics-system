def generate_report(
    total_revenue,
    region_sales,
    top_products,
    top_customers,
    daily_sales,
    output_path="output/sales_report.txt"
):
    with open(output_path, "w") as f:
        f.write("SALES ANALYTICS REPORT\n")
        f.write("======================\n\n")

        f.write(f"Total Revenue: {total_revenue}\n\n")

        f.write("Revenue by Region:\n")
        for region, amount in region_sales.items():
            f.write(f"- {region}: {amount}\n")

        f.write("\nTop Selling Products:\n")
        for product, qty in top_products:
            f.write(f"- {product}: {qty} units\n")

        f.write("\nTop Customers:\n")
        for customer, amount in top_customers:
            f.write(f"- {customer}: {amount}\n")

        f.write("\nDaily Sales Trend:\n")
        for date, amount in daily_sales.items():
            f.write(f"- {date}: {amount}\n")
