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
    ("https://static.wixstatic.com/media/181faa_3ef139005f3249f19befef0e7336e9d9~mv2.jpg/v1/fill/w_1960,h_1308,al_c,q_90,usm_0.66_1.00_0.01,enc_avif,quality_auto/L1010447_JPG.jpg", "paradise.jpg"),

    # Le Petit Echo de la Mode
    ("https://static.wixstatic.com/media/181faa_2257faa800774fe4a8d1d9bf651051c6~mv2.jpg/v1/fill/w_540,h_717,al_c,lg_1,q_85,enc_avif,quality_auto/181faa_2257faa800774fe4a8d1d9bf651051c6~mv2.jpg", "petitecho_1.jpg"),
    ("https://static.wixstatic.com/media/181faa_b1eca72b9a3a452d842a124b5c9329ba~mv2.png/v1/fill/w_372,h_720,al_c,lg_1,q_85,enc_avif,quality_auto/181faa_b1eca72b9a3a452d842a124b5c9329ba~mv2.png", "petitecho_poster.png"),
    ("https://static.wixstatic.com/media/181faa_576d78bf3f7643ca97efd4be47e4d3fe~mv2.jpg/v1/fill/w_720,h_480,al_c,lg_1,q_80,enc_avif,quality_auto/181faa_576d78bf3f7643ca97efd4be47e4d3fe~mv2.jpg", "petitecho_2.jpg"),
    ("https://static.wixstatic.com/media/181faa_f6cf38bde7984d74a43acba9825ac3c2~mv2.jpg/v1/fill/w_626,h_540,al_c,lg_1,q_80,enc_avif,quality_auto/181faa_f6cf38bde7984d74a43acba9825ac3c2~mv2.jpg", "petitecho_3.jpg"),
    ("https://static.wixstatic.com/media/181faa_1a88c8b8dcc6489886017a8595f4e11b~mv2.jpeg/v1/fill/w_540,h_702,al_c,lg_1,q_85,enc_avif,quality_auto/181faa_1a88c8b8dcc6489886017a8595f4e11b~mv2.jpeg", "petitecho_4.jpeg"),

    # Huis Clos
    ("https://static.wixstatic.com/media/181faa_8736e6037e97495981eb8f77f5721669~mv2.png/v1/fill/w_483,h_720,al_c,lg_1,q_85,enc_avif,quality_auto/Capture%20d%E2%80%99%C3%A9cran%202023-08-26%20%C3%A0%2014_46_46.png", "huisclos_affiche.png"),
    ("https://static.wixstatic.com/media/181faa_d4a47bf504394eaebfdc46d4a24caa40~mv2.jpg/v1/fill/w_540,h_719,al_c,lg_1,q_85,enc_avif,quality_auto/181faa_d4a47bf504394eaebfdc46d4a24caa40~mv2.jpg", "huisclos_1.jpg"),
    ("https://static.wixstatic.com/media/181faa_792c07b1a7d841b692e6c712d7532d6b~mv2.jpg/v1/fill/w_536,h_720,al_c,lg_1,q_85,enc_avif,quality_auto/181faa_792c07b1a7d841b692e6c712d7532d6b~mv2.jpg", "huisclos_2.jpg"),
    ("https://static.wixstatic.com/media/181faa_75572788cdcc497d9af593965072728a~mv2.jpeg/v1/fill/w_540,h_716,al_c,lg_1,q_85,enc_avif,quality_auto/181faa_75572788cdcc497d9af593965072728a~mv2.jpeg", "huisclos_3.jpeg"),
    ("https://static.wixstatic.com/media/181faa_5c56c51691b44cf7858677047160c5f3~mv2.jpg/v1/fill/w_355,h_595,al_c,lg_1,q_80,enc_avif,quality_auto/181faa_5c56c51691b44cf7858677047160c5f3~mv2.jpg", "huisclos_4.jpg"),
    ("https://static.wixstatic.com/media/181faa_49d53a24c272472396c269b9d87c4f09~mv2.jpg/v1/fill/w_332,h_498,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/181faa_49d53a24c272472396c269b9d87c4f09~mv2.jpg", "huisclos_5.jpg"),
    ("https://static.wixstatic.com/media/181faa_bb320c10baa743418cdc233e3a79030b~mv2.jpg/v1/fill/w_752,h_498,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/181faa_bb320c10baa743418cdc233e3a79030b~mv2.jpg", "huisclos_6.jpg"),
    ("https://static.wixstatic.com/media/181faa_34aeed4cf5854963ac624ffdc70df539~mv2.jpg/v1/fill/w_716,h_479,al_c,lg_1,q_80,enc_avif,quality_auto/181faa_34aeed4cf5854963ac624ffdc70df539~mv2.jpg", "huisclos_7.jpg"),
    ("https://static.wixstatic.com/media/181faa_91e4d6d855144261b78667600d769c11~mv2.jpg/v1/fill/w_344,h_520,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/181faa_91e4d6d855144261b78667600d769c11~mv2.jpg", "huisclos_8.jpg"),
    ("https://static.wixstatic.com/media/181faa_406d10f5e4344c008ffd56d556332cfa~mv2.jpg/v1/fill/w_752,h_498,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/181faa_406d10f5e4344c008ffd56d556332cfa~mv2.jpg", "huisclos_9.jpg"),
    ("https://static.wixstatic.com/media/181faa_c9991e8a70234a29a0307f001e5e1487~mv2.jpg/v1/fill/w_716,h_479,al_c,lg_1,q_80,enc_avif,quality_auto/181faa_c9991e8a70234a29a0307f001e5e1487~mv2.jpg", "huisclos_10.jpg"),

    # Collection de carte du monde
    ("https://static.wixstatic.com/media/181faa_def765bbc63a41d685135d84c693e84b%7Emv2_d_4928_3264_s_4_2.jpg/v1/fit/w_2500,h_1330,al_c/181faa_def765bbc63a41d685135d84c693e84b%7Emv2_d_4928_3264_s_4_2.jpg", "saotome.jpg"), # Placeholder if same
    
    # Résidences
    ("https://static.wixstatic.com/media/181faa_39cfa812d532401bba5845f9eb2bdc16~mv2.png/v1/fill/w_225,h_225,al_c/181faa_39cfa812d532401bba5845f9eb2bdc16~mv2.png", "casablanca.png"),
    ("https://static.wixstatic.com/media/181faa_51501d2d3efe4a9bad48500e57147c9a~mv2.jpg/v1/fill/w_1280,h_852,al_c/181faa_51501d2d3efe4a9bad48500e57147c9a~mv2.jpg", "inde.jpg"),
    ("https://static.wixstatic.com/media/181faa_e23289f62ffa48faa4f591d7e39eb0b0~mv2.jpg/v1/fill/w_2500,h_3333,al_c/181faa_e23289f62ffa48faa4f591d7e39eb0b0~mv2.jpg", "centrebretagne.jpg"),
    ("https://static.wixstatic.com/media/181faa_86ba220f94a34e42926686ef5c2b2233~mv2_d_3264_2448_s_4_2.jpg/v1/fill/w_2500,h_1875,al_c/181faa_86ba220f94a34e42926686ef5c2b2233~mv2_d_3264_2448_s_4_2.jpg", "maroc.jpg"),
    
    # Séries
    ("https://static.wixstatic.com/media/181faa_c70a904e3c2147bca475c9a6e63cf79d~mv2.jpg/v1/fill/w_2500,h_3333,al_c/181faa_c70a904e3c2147bca475c9a6e63cf79d~mv2.jpg", "confinement.jpg")
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
