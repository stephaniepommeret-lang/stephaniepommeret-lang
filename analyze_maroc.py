import re

with open('maroc_raw.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all image tags
img_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', re.IGNORECASE)
# Also find Wix image data usually in JSON or specific attributes
wix_img_pattern = re.compile(r'"uri":"([^"]+)","filename":"([^"]+)"', re.IGNORECASE)

print("--- Standard Images ---")
for match in img_pattern.finditer(content):
    print(f"SRC: {match.group(1)}")
    print(f"ALT: {match.group(2)}")
    print("-" * 20)

print("\n--- Wix Images (JSON/Attributes) ---")
# This is a heuristic to find high-res images often buried in Wix sites
for match in wix_img_pattern.finditer(content):
    print(f"URI: {match.group(1)}")
    print(f"Filename: {match.group(2)}")
    print("-" * 20)

# Try to find text blocks to see where they are relative to images
print("\n--- Text Blocks ---")
text_pattern = re.compile(r'>([^<]{20,})<')
for match in text_pattern.finditer(content):
    text = match.group(1).strip()
    if text and not "function" in text and not "var " in text:
        print(f"TEXT: {text[:100]}...")
