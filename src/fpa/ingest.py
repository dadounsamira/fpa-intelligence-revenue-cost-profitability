import requests
from pathlib import Path
import zipfile

TABLE_ID = "33100226"
RAW_DIR = Path("data/raw")
API_URL = "https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{table}/en"
FALLBACK_URL = "https://www150.statcan.gc.ca/n1/tbl/csv/{table}-eng.zip"
TIMEOUT_SECONDS = 60


def find_download_url(table_id):
    """Return the address of the table's CSV zip file."""
    try:
        response = requests.get(API_URL.format(table=table_id), timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        return response.json()["object"]
    except (requests.RequestException, KeyError, ValueError) as error:
        print("Web service failed:", error)
        return FALLBACK_URL.format(table=table_id)


def download_zip(url, destination):
    """Download the file at `url` and save it at `destination`."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    destination.write_bytes(response.content)
    return destination


zip_path = download_zip(find_download_url(TABLE_ID), RAW_DIR / f"{TABLE_ID}-eng.zip")
print("Saved to:", zip_path)

def unpack_zip(zip_path):
    """Extract the zip into RAW_DIR and return the paths of the files inside."""
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(RAW_DIR)
        names = archive.namelist()
    return [RAW_DIR / name for name in names]
for path in unpack_zip(zip_path):
    print("Extracted:", path)