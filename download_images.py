import os
import requests
from urllib.parse import urlparse

# Ensure images directory exists
if not os.path.exists('images'):
    os.makedirs('images')

images_to_download = [
    # Home
    ("https://static.wixstatic.com/media/181faa_def765bbc63a41d685135d84c693e84b%7Emv2_d_4928_3264_s_4_2.jpg/v1/fit/w_2500,h_1330,al_c/181faa_def765bbc63a41d685135d84c693e84b%7Emv2_d_4928_3264_s_4_2.jpg", "home-hero.jpg"),
    
    # Icons
    ("https://static.wixstatic.com/media/d3470ec8ca26475da4b228f0199b5d3d.png/v1/fill/w_50,h_50,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/d3470ec8ca26475da4b228f0199b5d3d.png", "facebook.png"),
    ("https://static.wixstatic.com/media/7177d158c36d432b93f51e54f80e2f3c.png/v1/fill/w_50,h_50,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/7177d158c36d432b93f51e54f80e2f3c.png", "instagram.png"),
    ("https://static.wixstatic.com/media/d7ffe259c9e54f59837481b3dd0130eb.png/v1/fill/w_50,h_50,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/d7ffe259c9e54f59837481b3dd0130eb.png", "soundcloud.png"),

    # Le Petit Echo de la Mode
    ("https://static.wixstatic.com/media/181faa_2257faa800774fe4a8d1d9bf651051c6~mv2.jpg/v1/fill/w_540,h_717,al_c,lg_1,q_85,enc_avif,quality_auto/181faa_2257faa800774fe4a8d1d9bf651051c6~mv2.jpg", "petit-echo.jpg"),

    # Paradise / Recherche Actuelle
    ("https://static.wixstatic.com/media/181faa_3ef139005f3249f19befef0e7336e9d9~mv2.jpg/v1/fill/w_1960,h_1308,al_c,q_90,usm_0.66_1.00_0.01,enc_avif,quality_auto/L1010447_JPG.jpg", "paradise.jpg")
]

for url, filename in images_to_download:
    print(f"Downloading {filename}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(f'images/{filename}', 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Saved to images/{filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
