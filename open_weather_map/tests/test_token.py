import sys
import os
current_file = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file))
sys.path.insert(0,project_root)

from configs.settings import url_mentah,api_token,city
import requests


url_lengkap = f'{url_mentah}/weather?q={city}&appid={api_token}'

print('testing openweathermap api\n','=' * 20)
try:
    response = requests.get(url_lengkap ,timeout=10)
    print(f'status code : {response.status_code}')
    print(f'response time : {response.elapsed.total_seconds()} second')

    if response.status_code == 200:
        data = response.json()
        print('berhasil')
        print(f'city : {data['name']}')
        print(f'temperature : {data['main']['temp']}k')
        print(f'weather : {data['weather'][0]['description']}k')

    elif response.status_code == 401:
        print('gagal menayambungkan ,api salah')
    elif response.status_code == 404:
        print('tidak berhasil menemukan')
    elif response.status_code == 429:
        print('terlalu banyak permintaan')
    else:
        print(f'error : {response.status_code}')
        print(f'response : {response.test[:200]}')

except requests.exceptions.timeout:
    print('terlalu lama...waktu habis')
except requests.exceptions.ConnectionError:
    print('koneksi gagal')
except Exception as e:
    print(f'kesalahan tak terduga {e}')

    
    
