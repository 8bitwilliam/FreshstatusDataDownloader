import requests
import json
import urllib3
from requests.auth import HTTPBasicAuth

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
API_KEY = "YOUR-API-KEY" # Repalce YOUR-API-KEY with your API Key
SUBDOMAIN = "YOUR-SUBDOMAIN" # Replace YOUR-SUBDOMAIN with your Subdomain
BASE_URL = "https://public-api.freshstatus.io/api/v1"


def fetch_all(endpoint):
    """Fetch all paginated records from Freshstatus."""
    data = []
    page = 1
    while True:
        url = f"{BASE_URL}/{endpoint}?page={page}"
        print(f"Requesting: {url}")
        try:
            response = requests.get(
                url,
                auth=HTTPBasicAuth(API_KEY, SUBDOMAIN),
                verify=True
            )
        except requests.exceptions.SSLError:
            print("SSL verification failed, continuing without verification...")
            response = requests.get(
                url,
                auth=HTTPBasicAuth(API_KEY, SUBDOMAIN),
                verify=False
            )

        if response.status_code != 200:
            print(f"Error fetching {endpoint}: {response.status_code} {response.text}")
            break

        payload = response.json()
        results = payload.get("results", [])
        if not results:
            break

        data.extend(results)
        if not payload.get("next"):
            break
        page += 1

    return data


def save_to_json(data, filename):
    """Save records to JSON."""
    if not data:
        print(f"No data found for {filename}")
        return
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} records to {filename}")

print("Fetching incidents...")
incidents = fetch_all("incidents")

print("Fetching maintenance...")
maintenance = fetch_all("maintenance")

# Save JSON
save_to_json(incidents, "incidents_full.json")
save_to_json(maintenance, "maintenance_full.json")

print("Export completed successfully.")
