import os
from ftplib import FTP
from dotenv import load_dotenv

load_dotenv()

FTP_HOST = os.getenv("ARUBA_FTP_HOST")
FTP_USER = os.getenv("ARUBA_FTP_USER")
FTP_PASS = os.getenv("ARUBA_FTP_PASS")
FTP_DIR = "/public_html/temp/"
PUBLIC_URL = "https://www.ingfabiofidone.it/temp/"


def upload_to_aruba(image_path):
    filename = os.path.basename(image_path)
    with open(image_path, "rb") as f:
        ftp = FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FTP_DIR)
        ftp.storbinary(f"STOR {filename}", f)
        ftp.quit()
    return PUBLIC_URL + filename
