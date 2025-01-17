import subprocess
import os

def main_menu():
    print("""                                                                                                         
                                                                                                         
#### ##    ## ########  #######  ########  #### 
 ##  ###   ## ##       ##     ## ##     ##  ##  
 ##  ####  ## ##       ##     ## ##     ##  ##  
 ##  ## ## ## ######   ##     ## ########   ##  
 ##  ##  #### ##       ##     ## ##     ##  ##  
 ##  ##   ### ##       ##     ## ##     ##  ##  
#### ##    ## ##        #######  ########  #### 

""")
    print("""                                                                                                   

""")
    print("Select an option:")
    print("1. Whois")
    print("2. Subdomain Enumeration")
    print("3. Directory Enumeration")
    print("4. Port Scanning")
    print("5. Email Info Gathering")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    return choice

def execute_script(choice):
    while True:
        if choice == '1':
            subprocess.call("python3 domaininfo.py", shell=True)
        elif choice == '2':
            subprocess.call("python3 subdomains.py", shell=True)
        elif choice == '3':
            subprocess.call("python3 directory.py", shell=True)
        elif choice == '4':
            subprocess.call("python3 port.py", shell=True)
        elif choice == '5':
            subprocess.call("python3 mail.py", shell=True)
        elif choice == '6':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")

        print("")  # Empty line for better readability
        choice = input("Press 'r' to return to the main menu or 'x' to exit: ")
        if choice.lower() == 'r':
            break
        elif choice.lower() == 'x':
            print("Exiting...")
            exit()

def main():
    while True:
        choice = main_menu()
        execute_script(choice)
        print("")  # Empty line for better readability

if __name__ == '__main__':
    main()