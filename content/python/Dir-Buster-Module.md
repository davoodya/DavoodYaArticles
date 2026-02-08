+++
title = "Dir-Buster-Module"
tags = ["Python", "Pentest_Tools", "Red_Team"]
Category = "Cyber Security, Python"
draft = false
+++

----
Certainly! Below is a simple directory busting tool written in Python. It reads a wordlist file and tries each word as a directory in a given URL by making HTTP requests.

### Code

```python
import requests
import sys
from concurrent.futures import ThreadPoolExecutor

def dir_buster(base_url, word):
    # Build the full URL
    url = f"{base_url.rstrip('/')}/{word.strip()}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Found: {url}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python dirbuster.py <url> <wordlist>")
        return

    base_url = sys.argv[1]
    wordlist_file = sys.argv[2]

    try:
        with open(wordlist_file, 'r') as file:
            words = file.readlines()
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_file}' not found.")
        return

    # Use ThreadPoolExecutor for concurrent requests
    with ThreadPoolExecutor(max_workers=10) as executor:
        for word in words:
            executor.submit(dir_buster, base_url, word)

if __name__ == "__main__":
    main()
```

### How to Run the Tool

1. Save the code to a file named `dirbuster.py`.

2. Run the program using the following command:

   ```bash
   python dirbuster.py <url> <wordlist>
   ```

   Replace `<url>` with the base URL you want to test (e.g., `http://example.com`), and `<wordlist>` with the path to your wordlist file.

### Example

```bash
python dirbuster.py http://example.com wordlist.txt
```

### Explanation

- **Main Function**: The main function reads the URL and wordlist file path from the command-line arguments. It then reads the wordlist file into a list of words.

- **ThreadPoolExecutor**: The `ThreadPoolExecutor` from the `concurrent.futures` module is used to handle multiple HTTP requests concurrently. This allows the tool to be more efficient by performing multiple checks at once.

- **dir_buster Function**: The `dir_buster` function constructs the full URL by appending each word from the wordlist to the base URL, and then it sends an HTTP GET request using the `requests` library. If the response status code is `200 OK`, it prints the found URL.

- **Error Handling**: The tool includes basic error handling for both file reading and HTTP requests.

### Requirements

To use this tool, you'll need the `requests` library. You can install it using pip if it's not already installed:

```bash
pip install requests
```

### Notes

- The tool only prints URLs that return a `200 OK` status. You can modify the `dir_buster` function to handle other status codes or customize the response handling.

- You can adjust the `max_workers` parameter in the `ThreadPoolExecutor` to control the number of concurrent threads, depending on your system and network capabilities.

This simple script can be expanded with more advanced features or customized to fit specific needs.