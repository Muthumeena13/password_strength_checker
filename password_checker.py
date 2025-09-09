import re
import hashlib
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from IPython.display import display
from tqdm import tqdm

# Configurable constants
API_TIMEOUT = 5
MAX_THREADS = 5

# Password strength check function
def check_password_strength(password):
    return {
        'length_ok': len(password) >= 8,
        'has_uppercase': any(c.isupper() for c in password),
        'has_number': any(c.isdigit() for c in password),
        'has_special_char': bool(re.search(r'[@$!%*?&]', password))
    }

# Efficient breach check with k-anonymity API
def check_pwned_password(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1pass[:5], sha1pass[5:]

    try:
        res = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}', timeout=API_TIMEOUT)
        res.raise_for_status()
        hashes = (line.split(':') for line in res.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
    except requests.RequestException:
        return -1  # Indicate error
    return 0

# Wrapper function to analyze a single password
def analyze_password(pw):
    strength = check_password_strength(pw)
    breach_count = check_pwned_password(pw)

    return {
        'Password': pw,
        'Length >=8': strength['length_ok'],
        'Has Uppercase': strength['has_uppercase'],
        'Has Number': strength['has_number'],
        'Has Special Char': strength['has_special_char'],
        'Times Breached': breach_count
    }

# Main function with threading and progress bar
def main():
    print("🔐 Advanced Password Strength & Breach Checker\n")

    # Get number of passwords
    while True:
        try:
            num = int(input("How many passwords do you want to check? "))
            if num > 0:
                break
            else:
                print("⚠ Please enter a positive integer.")
        except ValueError:
            print("⚠ Invalid input. Enter an integer.")

    passwords = [input(f"Enter password #{i+1}: ") for i in range(num)]

    results = []
    print("\n⏳ Checking passwords (this may take a few seconds)...\n")

    # Use ThreadPoolExecutor for parallel API calls
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_to_pw = {executor.submit(analyze_password, pw): pw for pw in passwords}
        for future in tqdm(as_completed(future_to_pw), total=len(passwords), desc="Processing"):
            res = future.result()
            results.append(res)

    # Display final report
    report_df = pd.DataFrame(results)
    print("\n✅ Final Password Analysis Report:\n")
    display(report_df)

# Run program
main()
