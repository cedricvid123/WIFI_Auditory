import csv
from datetime import datetime

def log_results_to_csv(networks, filename="wifi_scan_results.csv"):
    """
    Logs the scan results to a CSV file. Creates the file if it doesn't exist.
    """
    # Define the header
    header = ["Timestamp", "SSID (Name)", "BSSID (MAC Address)", "Signal Strength (dBm)", "Encryption Type"]

    # Open the file in append mode ('a+')
    with open(filename, mode='a+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Move to the beginning of the file to check if it's empty
        file.seek(0)
        first_char = file.read(1)

        # If the file is empty, write the header
        if not first_char:
            writer.writerow(header)

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write each network to the CSV
        for network in networks:
            writer.writerow([
                timestamp,
                network["SSID"],
                network["BSSID"],
                network["Signal"],
                network["Encryption"]
            ])
    
    print(f"\n✅ Results successfully logged to {filename}")
