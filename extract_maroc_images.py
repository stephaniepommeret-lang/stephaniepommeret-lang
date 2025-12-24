import json
import re

with open('maroc_raw.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Try to find the warmup data
warmup_pattern = re.compile(r'<script type="application/json" id="wix-warmup-data">(.+?)</script>')
match = warmup_pattern.search(content)

if match:
    try:
        data = json.loads(match.group(1))
        # Traverse the JSON to find gallery items
        def find_items(obj):
            if isinstance(obj, dict):
                if 'items' in obj and isinstance(obj['items'], list):
                    for item in obj['items']:
                        if isinstance(item, dict) and 'mediaUrl' in item:
                            print(f"IMAGE: {item['mediaUrl']}")
                            if 'metaData' in item:
                                meta = item['metaData']
                                print(f"TITLE: {meta.get('title', '')}")
                                print(f"DESC: {meta.get('description', '')}")
                            print("-" * 20)
                for key, value in obj.items():
                    find_items(value)
            elif isinstance(obj, list):
                for item in obj:
                    find_items(item)
        
        print("--- EXTRACTED ITEMS ---")
        find_items(data)
    except json.JSONDecodeError:
        print("Failed to decode JSON")
else:
    print("No warmup data found")
