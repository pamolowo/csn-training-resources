## Integrating VirusTotal API
import os
from dotenv import load_dotenv
import requests

load_dotenv()
xapikey = os.getenv('API_KEY')
scan_url = "example.com"

def analysis_report(analysis_id):
    report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    headers = {
        "x-apikey": xapikey
    }
    res = requests.get(report_url, headers=headers)
    # print("Analysis response: ", res.json())
    report = res.json()
    results = report['data']['attributes']['results']
    print(f"Analysis response for {scan_url}:", results.get('Fortinet'))
    
def urlscan(url):
    BASE_URL = "https://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": xapikey
    }
    
    req_url = requests.utils.quote(url, safe='')
    # res = requests.get(f"{BASE_URL}/{req_url}", headers=headers)
    
    data = {
        "url": req_url
    }
    
    res = requests.post(BASE_URL, headers=headers, data=data)
    analysis_id = res.json()['data']['id']
    analysis_report(analysis_id)
    # print("API response: ", res.json())

urlscan(scan_url)
