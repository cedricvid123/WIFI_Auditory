import os
import subprocess
from scanner.scanner import WiFiScanner
from crack.cracker import WiFiCracker
from capture.capturer import PacketCapturer
from reports.report_generator import ReportGenerator

def main():
    print(""" 
    ======================================
            Wi-Fi Security Auditor
    ======================================
    1. Scan for Wi-Fi Networks
    2. Capture Handshake Packets
    3. Crack Wi-Fi Password
    4. Generate Report
    5. Exit
    """)

    scanner = WiFiScanner()
    capturer = PacketCapturer()
    cracker = WiFiCracker()
    reporter = ReportGenerator()

    while True:
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("Scanning for Wi-Fi Networks...")
            scanner.scan()
        
        elif choice == '2':
            ssid = input("Enter the SSID to capture handshake: ")
            print(f"Capturing packets for {ssid}...")
            capturer.capture(ssid)
        
        elif choice == '3':
            handshake_file = input("Enter the handshake file path: ")
            wordlist = input("Enter the wordlist path: ")
            print(f"Attempting to crack password for {handshake_file}...")
            cracker.crack(handshake_file, wordlist)
        
        elif choice == '4':
            print("Generating Report...")
            reporter.generate()
        
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    main()
""
