"""
Konfigurasi terpusat
"""

BASE_URL = "https://www.googleapis.com"
SEND_ENDPOINT = "/identitytoolkit/v3/relyingparty/getOobConfirmationCode"
VERIFY_ENDPOINT = "/identitytoolkit/v3/relyingparty/signInWithCustomToken"

API_KEY = "AIzaSyDtG1AU22ErnQD60AzBAcaknySiz9_CEq0"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 15)",
    "X-Android-Package": "com.alightcreative.motion",
    "X-Android-Cert": "ECA6BF91B8715A6F810ED0BBFC65B6CD578F52A8"
}
