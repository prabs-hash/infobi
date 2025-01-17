import subprocess

def main():
    domain_name = input("Enter the domain name: ")
    result = subprocess.run(['whois', domain_name], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    main()
