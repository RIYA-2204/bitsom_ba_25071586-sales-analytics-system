def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues
    Returns: list of raw lines (strings)
    """
    encodings = ["utf-8", "latin-1", "cp1252"]

    for encoding in encodings:
        try:
            with open(filename, "r", encoding=encoding) as file:
                lines = file.readlines()

            # Skip header and remove empty lines
            clean_lines = []
            for line in lines[1:]:  # skip header
                if line.strip():
                    clean_lines.append(line.strip())

            return clean_lines

        except FileNotFoundError:
            print("Error: sales data file not found.")
            return []

        except Exception:
            # try next encoding
            continue

    print("Error: Unable to read file with supported encodings.")
    return []
