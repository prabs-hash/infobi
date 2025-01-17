import requests
import json

# Hunter.io API key
API_KEY = ""

# Prompt the user for the target organization
organization = input("Enter the target organization (e.g., example.com): ")

# Perform email reconnaissance
url = f"https://api.hunter.io/v2/domain-search?domain={organization}&api_key={API_KEY}"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    emails = data.get("data", {}).get("emails", [])
    
    # Check if any emails were found
    if emails:
        print(f"\nEmails found for domain {organization}:\n")
        for idx, email_info in enumerate(emails, start=1):
            email = email_info.get("value", "N/A")
            first_name = email_info.get("first_name", "N/A")
            last_name = email_info.get("last_name", "N/A")
            position = email_info.get("position", "N/A")
            confidence = email_info.get("confidence", "N/A")
            department = email_info.get("department", "N/A")
            
            # Print the details of each email in a formatted way
            print(f"Email #{idx}:")
            print(f"  Email Address: {email}")
            print(f"  First Name   : {first_name}")
            print(f"  Last Name    : {last_name}")
            print(f"  Position     : {position}")
            print(f"  Confidence   : {confidence}")
            print(f"  Department   : {department}")
            print("-" * 40)
    else:
        print(f"No emails found for domain {organization}.")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
