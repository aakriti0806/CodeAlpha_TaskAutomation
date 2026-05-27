import requests
from bs4 import BeautifulSoup
import os

# ---- SETTINGS ----
websites = [
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://www.github.com"
]
output_file = "C:/Users/HP/Desktop/PROJECT/CodeAlpha_TaskAutomation/scraped_titles.txt"
# ------------------

print("🌐 Web Title Scraper Started")
print("-" * 40)

results = []

for url in websites:
    try:
        # Send request to website
        response = requests.get(url, timeout=5)
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Get the title
        title = soup.title.string.strip() if soup.title else "No title found"
        
        print(f"✅ {url}")
        print(f"   Title: {title}\n")
        
        results.append(f"URL: {url}\nTitle: {title}\n")

    except Exception as e:
        print(f"❌ Failed to fetch {url} → {e}\n")
        results.append(f"URL: {url}\nTitle: ERROR - {e}\n")

# Save results to file
with open(output_file, "w") as f:
    f.write("Scraped Web Titles\n")
    f.write("=" * 30 + "\n\n")
    for result in results:
        f.write(result + "-" * 30 + "\n")

print(f"🎉 Done! Results saved to '{output_file}'")