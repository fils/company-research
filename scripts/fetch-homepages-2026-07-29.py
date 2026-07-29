#!/usr/bin/env python3
"""Fetch homepage text for candidate companies."""
import re, subprocess
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
        self._skip_tags = {"script", "style", "noscript", "svg"}

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self._skip_tags:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag.lower() in self._skip_tags and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            t = data.strip()
            if t:
                self.parts.append(t)


def fetch(url, limit=5000):
    try:
        raw = subprocess.check_output(
            ["curl", "-sL", "-A", "Mozilla/5.0", "--max-time", "30", url],
            stderr=subprocess.DEVNULL,
        )
        text = raw.decode("utf-8", "replace")
        p = TextExtractor()
        p.feed(text)
        out = re.sub(r"\s+", " ", " ".join(p.parts))
        return out[:limit]
    except Exception as e:
        return f"ERR {e}"


URLS = [
    ("ENDURANCE", "https://www.enduranceenergy.com/"),
    ("KRAKEN", "https://krakentechnology.com/"),
    ("KRAKEN_NEWS", "https://krakentechnology.com/articles/kraken-technology-group-raises-160m-at-1bn-valuation"),
    ("XOCEAN", "https://xocean.com/"),
    ("SAILDRONE", "https://www.saildrone.com/"),
    ("SAILDRONE_ABOUT", "https://www.saildrone.com/about"),
    ("TECHCRUNCH_ENDURANCE", "https://techcrunch.com/2026/06/11/endurance-energy-raises-54m-to-harness-a-massive-untapped-energy-source/"),
    ("ROBOT_KRAKEN", "https://www.therobotreport.com/kraken-technology-raises-series-b-funding-autonomous-vessels/"),
    ("XOCEAN_PR", "https://www.prnewswire.com/news-releases/xocean-secures-115-million-investment-to-accelerate-growth-of-its-ocean-data-services-platform-302346644.html"),
]

if __name__ == "__main__":
    for name, url in URLS:
        print("====", name, "====")
        print(fetch(url))
        print()
