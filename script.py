from datetime import datetime

def write_time_to_file():
    """Writes the current timestamp to a unique text file every minute."""
    # Generate timestamp for filename (YYYYMMDD_HHMM format)
    filename_time = datetime.now().strftime("%Y%m%d_%H%M")
    file_name = f"timestamp_{filename_time}.txt"

    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the timestamp to the file
    with open(file_name, "w") as file:
        file.write(f"{current_time}\n")

    print(f"✅ Time written to file: {file_name}")

if __name__ == "__main__":
    write_time_to_file()
