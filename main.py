#!/usr/bin/env python3
"""
AM Premium Generator
Tool aktivasi Alight Motion Premium via magic link
"""

import sys
import time
from config import BASE_URL, SEND_ENDPOINT, VERIFY_ENDPOINT, API_KEY, HEADERS

try:
    import requests
except ImportError:
    print("[X] Module 'requests' belum keinstall.")
    print("    Jalanin: pip install requests")
    sys.exit(1)


def kirim_magic_link(email):
    """Kirim magic link ke email target"""
    url = f"{BASE_URL}{SEND_ENDPOINT}"
    payload = {
        "email": email,
        "apiKey": API_KEY,
        "returnSecureToken": True
    }
    
    print(f"[1/2] Ngirim magic link ke: {email}")
    try:
        r = requests.post(url, json=payload, headers=HEADERS, timeout=30)
        print(f"      Status: {r.status_code}")
        return r
    except requests.exceptions.Timeout:
        print("[X] Timeout. Server gak respon.")
        return None
    except Exception as e:
        print(f"[X] Error: {e}")
        return None


def verifikasi_link(email, link):
    """Verifikasi magic link buat aktifin premium"""
    url = f"{BASE_URL}{VERIFY_ENDPOINT}"
    payload = {
        "email": email,
        "link": link,
        "apiKey": API_KEY
    }
    
    print(f"[2/2] Verifikasi link...")
    try:
        r = requests.post(url, json=payload, headers=HEADERS, timeout=30)
        print(f"      Status: {r.status_code}")
        return r
    except Exception as e:
        print(f"[X] Error: {e}")
        return None


def main():
    print("=" * 40)
    print("  AM PREMIUM GENERATOR")
    print("=" * 40)
    print()
    
    email = input("Email target: ").strip()
    
    if not email or "@" not in email:
        print("[X] Email gak valid.")
        return
    
    # Step 1
    hasil_kirim = kirim_magic_link(email)
    if not hasil_kirim:
        return
    
    print()
    print("=" * 40)
    print("  BUKA EMAIL LU SEKARANG")
    print("=" * 40)
    print("1. Cek inbox (atau folder Spam/Promosi)")
    print("2. Cari email dari Alight Motion")
    print("3. Copy magic link di email itu")
    print("=" * 40)
    print()
    
    # Cooldown
    print("Cooldown 15 detik...")
    for i in range(15, 0, -1):
        print(f"  {i}...", end="\r")
        time.sleep(1)
    print()
    
    link = input("Tempel magic link: ").strip()
    
    if not link.startswith("https://"):
        print("[X] Link harus diawali https://")
        return
    
    # Step 2
    hasil_verify = verifikasi_link(email, link)
    
    print()
    if hasil_verify and hasil_verify.status_code == 200:
        print("[ SUKSES ] Premium aktif!")
    else:
        print("[ GAGAL ] Cek kembali linknya.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Dibatalkan.")