"""Génère les images de partage (Open Graph / Twitter) au format 1200 × 630.

Pour chaque image déclarée dans le front matter (`image.path`), crée
images/og/<nom>.jpg : l'œuvre entière, centrée sur le fond blanc du site,
sans recadrage ni agrandissement. _includes/seo.html utilise ce fichier
pour og:image et twitter:image dès qu'il existe ; les données structurées
continuent de pointer vers l'image d'origine.

Utilisation : python3 _scripts/og_images.py   (depuis la racine du dépôt)
"""

from pathlib import Path
import re

from PIL import Image

WIDTH, HEIGHT = 1200, 630
BACKGROUND = (255, 255, 255)
ROOT = Path(__file__).resolve().parent.parent
SOURCES = ["*.md", "_expositions/*.md", "_residences/*.md", "_photos/*.md"]


def declared_images():
    paths = set()
    for pattern in SOURCES:
        for page in ROOT.glob(pattern):
            text = page.read_text(encoding="utf-8")
            front = text.split("---", 2)[1] if text.startswith("---") else ""
            match = re.search(r"^image:\s*\n\s+path:\s*(\S+)", front, re.M)
            if match:
                paths.add(match.group(1).strip("\"'"))
    return sorted(paths)


def card(source: Path, target: Path):
    with Image.open(source) as image:
        image = image.convert("RGB")
        scale = min(WIDTH / image.width, HEIGHT / image.height, 1)
        size = (round(image.width * scale), round(image.height * scale))
        if size != image.size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
        canvas.paste(image, ((WIDTH - size[0]) // 2, (HEIGHT - size[1]) // 2))
        target.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(target, "JPEG", quality=84, optimize=True, progressive=True)


def main():
    for path in declared_images():
        source = ROOT / path.lstrip("/")
        target = ROOT / "images" / "og" / (source.stem + ".jpg")
        card(source, target)
        print(f"{path} -> {target.relative_to(ROOT)} ({target.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
