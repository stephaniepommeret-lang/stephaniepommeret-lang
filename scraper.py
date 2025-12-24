import os
import re
import requests
from urllib.parse import urljoin, urlparse

TARGET_URL = "https://www.stephaniepommeret.com/recherche-actuelle"
OUTPUT_FILE = "recherche-actuelle.html"
ASSETS_DIR = "recherche_assets"

# Create assets directory
if not os.path.exists(ASSETS_DIR):
    os.makedirs(ASSETS_DIR)

def download_asset(url):
    try:
        # Get filename from URL, handle query parameters
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename or "." not in filename:
            # Fallback for weird URLs
            filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', url)
            if len(filename) > 50:
                filename = filename[-50:]
            if not os.path.splitext(filename)[1]:
                filename += ".asset"
        
        # Handle duplicate filenames
        filepath = os.path.join(ASSETS_DIR, filename)
        if os.path.exists(filepath):
            # easy simple dedup if content is different? 
            # for now, assume same name = same file or overwrite is fine
            pass # print(f"Exists: {filename}")
        else:
            print(f"Downloading: {url} -> {filename}")
            r = requests.get(url, stream=True, timeout=10)
            if r.status_code == 200:
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            else:
                print(f"Failed to fetch {url} (Status {r.status_code})")
                return url # return original if failed

        return f"{ASSETS_DIR}/{filename}"
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return url

def main():
    print(f"Fetching {TARGET_URL}...")
    try:
        response = requests.get(TARGET_URL)
        response.raise_for_status()
        html_content = response.text
    except Exception as e:
        print(f"Failed to fetch page: {e}")
        return

    # Simple regex to find src and href
    # We look for src="..." or href="..."
    # We capture the quote type to ensure we close it matching
    # Group 1: src or href
    # Group 2: quote
    # Group 3: url
    pattern = re.compile(r'(src|href|content)=([\'"])(https?://[^"\']+\.(?:png|jpg|jpeg|gif|css|js|ico|svg|woff|woff2|json)(?:[^"\']*)?)\2', re.IGNORECASE)

    def replace_match(match):
        attr = match.group(1)
        quote = match.group(2)
        url = match.group(3)
        
        # Filter: only download assets that look like assets. 
        # Wix might have absolute links to other pages, we don't want to rewrite those unless they are resources.
        # The regex above filters for extensions.
        
        local_path = download_asset(url)
        return f'{attr}={quote}{local_path}{quote}'

    new_html = pattern.sub(replace_match, html_content)

    # Also look for background-image: url(...)
    css_url_pattern = re.compile(r'url\([\'"]?(https?://[^)]+\.(?:png|jpg|jpeg|gif|svg)(?:[^)]*)?)[\'"]?\)', re.IGNORECASE)
    
    def replace_css_url(match):
        url = match.group(1)
        local_path = download_asset(url)
        return f'url("{local_path}")'

    new_html = css_url_pattern.sub(replace_css_url, new_html)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"Done! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
