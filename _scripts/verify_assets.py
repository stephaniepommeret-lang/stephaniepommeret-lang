"""Vérifie les ressources locales du site généré.

Utilisation : python3 _scripts/verify_assets.py [_site]
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("src"):
            self.references.append(attrs["src"])
        if attrs.get("srcset"):
            self.references.extend(
                match.group(1).rstrip(",")
                for match in re.finditer(r"(?:^|,\s*)(\S+)", attrs["srcset"])
            )
        if tag == "link" and attrs.get("rel") in {"icon", "apple-touch-icon", "stylesheet", "preload"}:
            self.references.append(attrs["href"])
        if tag == "meta" and attrs.get("property") in {"og:image", "twitter:image"}:
            self.references.append(attrs["content"])
        if tag == "meta" and attrs.get("name") == "twitter:image":
            self.references.append(attrs["content"])
        if attrs.get("data-swiper-css"):
            self.references.append(attrs["data-swiper-css"])
        self.in_style = tag == "style"

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False

    def handle_data(self, data):
        # Feuille de style intégrée : polices et images appelées par url().
        if getattr(self, "in_style", False):
            self.references.extend(
                match.group(2)
                for match in re.finditer(r"url\((['\"]?)([^'\")]+)\1\)", data)
                if not match.group(2).startswith("data:")
            )


def main():
    cli = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    cli.add_argument("site", nargs="?", type=Path, default=Path("_site"))
    options = cli.parse_args()
    site = options.site
    html_pages = sorted(site.rglob("*.html"))
    if not html_pages:
        cli.error(f"aucune page HTML dans {site}")

    domain = (site / "CNAME").read_text(encoding="utf-8").strip()
    missing = []
    verified = 0
    for page in html_pages:
        path = page.relative_to(site).as_posix()
        assets = Assets()
        assets.feed(page.read_text(encoding="utf-8"))
        for reference in assets.references:
            url = urlsplit(urljoin(f"https://{domain}/{path}", reference))
            if url.hostname != domain or url.scheme not in {"http", "https"}:
                continue
            verified += 1
            asset = site / unquote(url.path).lstrip("/")
            if not asset.is_file() or asset.stat().st_size == 0:
                missing.append(f"{path} : {reference}")

    if missing:
        print("\n".join(missing))
        return 1
    print(f"{verified} références locales valides dans {len(html_pages)} pages HTML.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
