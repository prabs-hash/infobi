import subprocess

def dirb_scan(domain):
    try:
        # Run dirb scan with specified domain
        subprocess.run(['dirb', domain])
    except FileNotFoundError:
        print("Error: dirb tool not found. Make sure dirb is installed and in your system's PATH.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    domain = input("Enter the domain url to perform directory enumeration: ")
    dirb_scan(domain)

if __name__ == "__main__":
    main()
