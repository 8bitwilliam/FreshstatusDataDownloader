# FreshstatusDataDownloader
Freshstatus Data Downloader is a Python script for exporting all incident and maintenance data from a Freshstatus public status page using the Freshstatus Public API. 

It automatically retrieves every available record and saves them locally as JSON files for backup, analysis, or migration to other platforms.

---

## Features
- Exports all **incidents** and **maintenance** records from your Freshstatus page  
- Saves data as JSON (`incidents_full.json`, `maintenance_full.json`)  
- Works on macOS, Linux, and Windows  
- Includes SSL fallback for systems missing CA certificates  

---

## Requirements
- Python **3.8+**
- `requests` library

Install with:
pip install requests

---

## Setup & Usage

Follow these steps to configure and run the downloader.

1  Create a virtual environment (only required once)
    python3 -m venv freshstatus

2 Activate the environment

    # macOS / Linux:

	source ~/freshstatus/bin/activate
    
	# Windows:
    
	freshstatus\Scripts\activate

3 Install dependencies
    pip install requests

4 Download or clone this repository

5 Edit the script and add your Freshstatus credentials:
    Open FreshstatusDownload.py and update these lines:
	
    API_KEY = "YOUR-API-KEY"
    
	SUBDOMAIN = "YOUR-SUBDOMAIN"

6 Run the script
    python3 ~/FreshstatusDownload.py

7 When complete, two files will be created:

    incidents_full.json

	maintenance_full.json

---

Notes
	•	Uses secure SSL verification by default, falling back to unverified mode if your system certificates are missing (common on macOS).
	•	Performs read-only operations, nothing is modified or deleted on Freshstatus.
	•	Requires an API key with access to the incidents and maintenance endpoints.
