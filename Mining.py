import random
import requests
import time

WEBHOOK = "WEBHOOK"

def R(length=18):
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=length))

def main():
    while True:
        code = R()
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            requests.post(WEBHOOK, json={"content": code})
            print(f"Valid code found: {code}")
        else:
            print(f"Invalid code: {code}")
        time.sleep(0.1)

if __name__ == "__main__":
    main()
