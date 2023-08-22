# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json

def get_numbers(urls):
    num = []
    for url in urls:
        resp = requests.get(url)
        if resp.status_code == 200:
            num.extend(resp.json()["numbers"])
    return sorted(list(set(num)))

def main():
    """The main function."""
    urls = [
        "http://20.244.56.144/numbers/primes",
        "http://20.244.56.144/numbers/fibo",
        "http://20.244.56.144/numbers/odd",
        "http://20.244.56.144/numbers/rand"
    ]

    num = get_numbers(urls)
    print(json.dumps({"numbers": num}))

if __name__ == "__main__":
    main()
