import urllib.request
import re

url = "http://www.socchina.net/details?id=2f2785641d6b484ea1ab859f05d9db85"

try:
    print(f"Fetching {url}...")
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8', errors='ignore')
        
    print(f"Page length: {len(html)}")
    
    # Look for .pdf links
    # Pattern to find href="..." where ... contains .pdf
    # This is a simple regex, might not catch all edge cases but good for research
    pdf_links = re.findall(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', html, re.IGNORECASE)
    
    print(f"Found {len(pdf_links)} PDF links.")
    for link in pdf_links:
        print(f"PDF Link: {link}")
        
    # Also look for any 'upload' or 'download' links just in case
    other_links = re.findall(r'href=["\']([^"\']*(?:upload|download)[^"\']*)["\']', html, re.IGNORECASE)
    print(f"Found {len(other_links)} other potential download links.")
    for link in other_links:
         if link not in pdf_links:
            print(f"Potentially relevant: {link}")

except Exception as e:
    print(f"Error: {e}")
