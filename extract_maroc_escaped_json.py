import json
import re
import html

with open('maroc_raw.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find JSON-like structures that might be escaped
# Looking for {"items": ... or similar gallery structures
# Often wix stores it in data-state or similar attributes
# Let's try to find large JSON blobs
pattern = re.compile(r'\{&quot;.*?\}(?:&quot;)?', re.DOTALL)

print("--- SEARCHING FOR JSON ---")
found_images = []

for match in pattern.finditer(content):
    raw = match.group(0)
    try:
        unescaped = html.unescape(raw)
        data = json.loads(unescaped)
        
        # Traverse found JSON
        def search_media(obj):
            if isinstance(obj, dict):
                if 'mediaUrl' in obj: # standard wix media object
                     found_images.append(obj)
                for k, v in obj.items():
                    search_media(v)
            elif isinstance(obj, list):
                for item in obj:
                    search_media(item)
        
        search_media(data)
    except:
        pass

# Also look for standard "items": [...] in unescaped content just in case
json_obj_pattern = re.compile(r'\{"items":\[.*?\]\}')
for match in json_obj_pattern.finditer(content):
     try:
        data = json.loads(match.group(0))
        for item in data.get('items', []):
            found_images.append(item)
     except:
         pass


print(f"Found {len(found_images)} images/media items")
seen_urls = set()
for img in found_images:
    url = img.get('mediaUrl', '')
    if not url: continue
    if url in seen_urls: continue
    seen_urls.add(url)
    
    meta = img.get('metaData', {})
    title = meta.get('title', '')
    desc = meta.get('description', '')
    
    print(f"URL: https://static.wixstatic.com/media/{url}")
    print(f"TITLE: {title}")
    print(f"DESC: {desc}")
    print("-" * 10)
