# CHEAT SHEET LIBRARY REQEUSTS 

## try-except timeout
```
import requests

url = "https://example.com"

try:
    # Coba request dengan timeout 5 detik
    response = requests.get(url, timeout=5)
    print("Berhasil! Status:", response.status_code)
    
except requests.exceptions.Timeout:
    # Terjadi jika waktu tunggu habis
    print("ERROR: Waktu tunggu habis! Internet lambat atau server down.")
    
except requests.exceptions.ConnectionError:
    # Terjadi jika tidak bisa konek sama sekali
    print("ERROR: Tidak bisa terhubung! Cek internet atau URL.")
    
except Exception as e:
    # Error lainnya
    print(f"ERROR Lainnya: {e}")
```

