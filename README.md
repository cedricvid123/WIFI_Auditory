# WIFI_Auditory
Wi-Fi security auditing is the process of analyzing, testing, and assessing the security posture of a wireless network to identify vulnerabilities, misconfigurations, and potential weaknesses that could be exploited by attackers.

# 1. Import Required Libraries

Explanation:

· pywifi: This library is used to interact with the WiFi interface.

· const: Contains constants for interface status and encryption.

· time: Allows for delays (useful while scanning for networks).

· prettytable: For displaying networks in a structured table format.

---

## Usage Examples
### Wi-Fi Scanning
To scan available Wi-Fi networks:
```bash
python main.py
```

### Packet Capturing
To capture handshake packets for a specific SSID:
```bash
python main.py
```
Follow the prompts to enter the SSID and begin capturing.

### Password Cracking
To attempt password cracking using a captured handshake:
```bash
python main_crack.py
```
Provide the handshake file and a wordlist when prompted.

### Report Generation
To generate a detailed report of findings:
```bash
python main.py
```
Select the option to generate a report. Output is saved to the `reports/` folder.

---

## Component Breakdown
- `scanner/`: Contains logic for discovering Wi-Fi networks.
- `capture/`: Handles the packet capturing process.
- `crack/`: Manages password cracking attempts.
- `reports/`: Generates structured reports of the audit.
- `ui/`: Manages user interface components.
- `utils/`: Contains helper functions for the application.

---

## System Requirements
- **OS:** Linux (Kali Linux recommended)
- **Python Version:** 3.8 or higher
- **Dependencies:** Listed in `requirements.txt`
- **Tools:** 
  - `aircrack-ng` for password cracking
  - `tcpdump` or `airodump-ng` for packet capturing

---

## Known Issues & Troubleshooting
1. **Wi-Fi Interface Not Found:**
   - Ensure your wireless adapter supports monitor mode.
   - Use `ifconfig` to check available interfaces.

2. **Handshake Not Captured:**
   - Make sure the target network has active devices.
   - Move closer to the access point if the signal is weak.

3. **Packet Capture Permission Denied:**
   - Run with `sudo` or as root:
     ```bash
     sudo python main.py
     ```

---

## Future Enhancements
- Add WPA3 handshake support.
- Implement de-authentication attack detection.
- Improve rogue AP detection accuracy.

---

Repository Structure

|-- capture/                # Handles packet capturing functionalities
|-- config/                 # Configuration files and settings
|-- crack/                  # Password cracking mechanisms
|-- reports/                # Generated audit reports
|-- scanner/                # Wi-Fi network scanning
|-- ui/                     # User interface components
|-- utils/                  # Utility functions
|-- main.py                 # Main entry point for the application
|-- main_crack.py           # Password cracking process
|-- crack_and_capture.py    # Integrated scanning, capturing, and cracking
|-- requirements.txt        # List of dependencies
|-- README.md               # Project documentation
|-- LICENSE                 # License information

---
# Installation

1. Clone the repository
   git clone https://github.com/cedricvid123/WIFI_Auditory.git
   cd wifi-security-auditor

2. Install dependencies:

   pip install -r requirements.txt

3. Ensure system tools are available (e.g., aircrack-ng):

   sudo apt-get install aircrack-ng

---

# Usage

# To scan available Wi-Fi networks:

python main.py

# Cracking Passwords

To initiate password cracking:

python main_crack.py

# Combined Capture and Crack

To perform packet capturing and password cracking:

python crack_and_capture.py
