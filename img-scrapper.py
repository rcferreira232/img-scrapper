import os
from icrawler.builtin import BingImageCrawler
from PIL import Image

# --- DESTINATION DIRECTORIES ---

BACKGROUND_DIR = "dataset/backgrounds"
OBJECT_DIR = "dataset/objects"

os.makedirs(BACKGROUND_DIR, exist_ok=True)
os.makedirs(OBJECT_DIR, exist_ok=True)

# --- SEARCH CONFIGURATION ---

BACKGROUND_QUERY = "background image"
OBJECT_QUERY = "apple on white background"

BACKGROUND_COUNT = 100
OBJECT_COUNT = 200

# --- DOWNLOAD BACKGROUND IMAGES ---

print("[START] Downloading background images...")

background_crawler = BingImageCrawler(
    storage={"root_dir": BACKGROUND_DIR}
)

background_crawler.crawl(
    keyword=BACKGROUND_QUERY,
    max_num=BACKGROUND_COUNT
)

# --- DOWNLOAD OBJECT IMAGES ---

print("\n[START] Downloading object images...")

object_crawler = BingImageCrawler(
    storage={"root_dir": OBJECT_DIR}
)

object_crawler.crawl(
    keyword=OBJECT_QUERY,
    max_num=OBJECT_COUNT
)

# --- POST-PROCESSING ---

print("\n[PROCESSING] Cleaning and organizing downloaded files...")

# Resize and convert background images to JPEG format

for filename in os.listdir(BACKGROUND_DIR):
    file_path = os.path.join(BACKGROUND_DIR, filename)

    try:
        with Image.open(file_path) as img:
            img = img.convert("RGB")
            img = img.resize((640, 640), Image.Resampling.LANCZOS)
            img.save(file_path, "JPEG")

    except Exception:
        if os.path.isfile(file_path):
            os.remove(file_path)

print("[DONE] All images were downloaded and processed successfully!")