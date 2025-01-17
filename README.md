# InfoBI - Information Gathering Tool

## Overview

InfoBI is a powerful information-gathering tool designed to simplify reconnaissance tasks for ethical hackers, security researchers, and penetration testers. The tool integrates various functionalities to collect critical information about a target, including:

- **WHOIS Lookup**: Retrieve domain registration and ownership details.
- **Port Scanning**: Identify open ports on a target system.
- **Subdomain Enumeration**: Discover subdomains associated with a target domain.
- **Email Information Gathering**: Extract email addresses and validate email details.
- **Directory Enumeration**: Identify accessible directories on a target web server.

## Features

- Simple command-line interface.
- Modular design for ease of use and extension.
- API integration with Hunter.io for email gathering.

## Installation Guide

Follow these steps to install and set up InfoBI on your system:

1. Clone the repository:
   ```bash
   $ git clone https://github.com/prabs-hash/infobi.git
   ```

2. Navigate to the project directory:
   ```bash
   $ cd infobi
   ```

3. Install the required Python dependencies:
   ```bash
   $ pip3 install -r requirements.txt
   ```

4. Configure the Hunter.io API:
   - Go to the [Hunter.io](https://hunter.io/) website.
   - Create an account to obtain your API key.
   - Open the `mail.py` file in a text editor and add your API key in the designated location.

5. Run the tool:
   ```bash
   $ python3 main.py
   ```

## Usage

InfoBI is designed to be straightforward. Upon running the tool, you will be guided through interactive prompts to select the desired information-gathering module and provide the necessary inputs.

## License

This project is licensed under the our License. Of course I have no license so its free for all.

## Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests.

## Contact

For any questions or suggestions, please contact [prabs-hash](https://github.com/prabs-hash/).

