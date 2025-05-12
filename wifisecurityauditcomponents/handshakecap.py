import subprocess # Used to run terminal commands in python

def capture_handshake(interface, bssid, channel, output_prefix):
    subprocess.run(['airodump-ng', '--bssid', bssid, '-c', channel, '-w', output_prefix, interface])


"""
    Runs airodump-ng to capture handshake packets for a specific Wi-Fi network.
    
    Parameters:
    - interface: the wireless network interface in monitor mode (like 'wlan0mon')
    - bssid: MAC address of the target Wi-Fi network
    - channel: the Wi-Fi channel the target network is on
    - output_prefix: the prefix for the capture file name

     Run the airodump-ng command with the specified parameters
    subprocess.run([
        'airodump-ng',         # Wi-Fi packet capturing tool
        '--bssid', bssid,      # Target network's BSSID (MAC address)
        '-c', channel,         # Channel the target network is operating on
        '-w', output_prefix,   # Prefix for the output capture file
        interface              # The monitor mode interface to use
    ])
"""

if __name__ == "__main__":
    # Test call with example values
    capture_handshake('wlan0mon', 'AA:BB:CC:DD:EE:FF', '6', 'test_capture')