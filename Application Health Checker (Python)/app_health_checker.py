import requests
from datetime import datetime

APP_URL = "http://localhost:8080"  # Change to your application URL
TIMEOUT = 5  # seconds

def check_application_health():
    print(f"\nChecking application health @ {datetime.now()}")

    try:
        response = requests.get(APP_URL, timeout=TIMEOUT)

        if 200 <= response.status_code < 300:
            print(f"Application Status: UP (HTTP {response.status_code})")
        else:
            print(f"Application Status: DOWN (HTTP {response.status_code})")

    except requests.exceptions.RequestException as e:
        print("Application Status: DOWN")
        print("Error:", e)

if __name__ == "__main__":
    check_application_health()
