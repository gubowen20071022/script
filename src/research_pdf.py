import requests
from bs4 import BeautifulSoup

url = "http://www.socchina.net/details?id=2f2785641d6b484ea1ab859f05d9db85"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print(f"Title: {soup.title.string if soup.title else 'No title'}")
    
    links = soup.find_all('a')
    print(f"Found {len(links)} links.")
    for link in links:
        href = link.get('href')
        if href:
            print(f"Link: {href}")
            if '.pdf' in href.lower():
                print(f"FOUND PDF: {href}")

except Exception as e:
    print(f"Error: {e}")
